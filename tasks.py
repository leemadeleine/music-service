from invoke import task

@task
def run(c):
    """
    Starts the local uvicorn webserver (for FastAPI)
    """
    c.run("uvicorn src.main:app --reload", pty=True)

#TODO: add auto formatting
