from sqlalchemy import create_engine, Column, DateTime, String, Text, Integer, text
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime
from function1 import mail_check

db_user = 'test_user'
db_password = 'test_password'
db_host = 'localhost'
db_name = 'test_db'

db_url = f"mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}"
engine = create_engine(db_url, echo=True)

Base = declarative_base()
Base.metadata.create_all(engine)
    
def dodaj_mail(sender, content):
    mail_status=mail_check([content])
    print(f"Prediction: {mail_status}")
    if mail_status == "ham":
        try:
            query = text("INSERT INTO mails_ham (received_date, sender, content) VALUES (:received_date, :sender, :content)")
            
            params = {
                "received_date": datetime.utcnow(),
                "sender": sender,
                "content": content
                }
            with engine.connect() as connection:
                connection.execute(query, params)
                connection.commit()

        except Exception as e:
            print(f"Error ham: {e}")
    else:
        try:
            query = text("INSERT INTO mails_spam (received_date, sender, content) VALUES (:received_date, :sender, :content)")
            
            params = {
                "received_date": datetime.utcnow(),
                "sender": sender,
                "content": content
                }
            with engine.connect() as connection:
                connection.execute(query, params)
                connection.commit()

        except Exception as e:
            print(f"Error spam: {e}")