from sqlalchemy import create_engine ,text
engine = create_engine("mysql+pymysql://root:root1225@talentquestdb.c5a4k64wsbb7.ap-south-1.rds.amazonaws.com/talentquestdb?charset=utf8mb4")

def load_jobs_from_db():
  with engine.connect() as conn:
    result = conn.execute(text("select * from jobs"))
    jobs = []
  for row in result.all():
    jobs.append(row._asdict())
  return jobs
  