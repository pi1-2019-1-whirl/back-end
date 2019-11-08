from flask.cli import FlaskGroup
from project import app , db
from project.api.water_box.model import WaterBox
from project.api.energy_log.model import EnergyLog


cli = FlaskGroup(app)

@cli.command()
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()

if __name__ == '__main__':
    cli()