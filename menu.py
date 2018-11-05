from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Restaurant, Base, MenuItem, User

engine = create_engine('sqlite:///restaurantmenu.db')
# Bind the engine to the metadata of the Base class so that the
# declaratives can be accessed through a DBSession instance
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
# A DBSession() instance establishes all conversations with the database
# and represents a "staging zone" for all the objects loaded into the
# database session object. Any change made against the objects in the
# session won't be persisted into the database until you call
# session.commit(). If you're not happy about the changes, you can
# revert all of them back to the last commit by calling
# session.rollback()
session = DBSession()

# Create dummy user
User1 = User(name="admin", email="saigalsaksham@gmail.com")
session.add(User1)
session.commit()

restaurant1 = Restaurant(name="Cafe JC", user_id="1")
session.add(restaurant1)
session.commit()

menuItem1 = MenuItem(name="Veg Sizzler",description="A combination of various snacks ",price="$5", restaurant=restaurant1, user_id=1)

session.add(menuItem1)
session.commit()
menuItem2 = MenuItem(name="Virgin Mojito",description=" Refreshing mocktail",price="$3",  restaurant=restaurant1, user_id=1)

session.add(menuItem2)
session.commit()


menuItem3 = MenuItem(name="Gelato", description="Ice cream" , price="$4.5", restaurant=restaurant1, user_id=1)

session.add(menuItem3)
session.commit()



restaurant2 = Restaurant(name="Nik Bakers")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Pasta",description="Fusilli pasta with red sauce", price="$9", restaurant=restaurant2)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Waffle",description="crunchy toasted mixture topped with ice cream and nutella",price="$5",  restaurant=restaurant2)

session.add(menuItem2)
session.commit()
menuItem3 = MenuItem(name="Red Velvet cake",description="Fresh cake ",price="$4", restaurant=restaurant2)
session.add(menuItem3)
session.commit()

restaurant3 = Restaurant(name="Haldirams")

session.add(restaurant2)
session.commit()


menuItem1 = MenuItem(name="Chana Bhature",description="Chicken peas cooked in tasty Indian Gravy along with fried bread.", price="$10", restaurant=restaurant3)

session.add(menuItem1)
session.commit()

menuItem2 = MenuItem(name="Chaat Papdi",description="Fresh Bhalla and papdi served with tamarind and green chutney",price="$6",  restaurant=restaurant3)

session.add(menuItem2)
session.commit()
menuItem3 = MenuItem(name="Dosa",description="Crunchy base made from rice, served with sambhar and coconut chutney ",price="$7", restaurant=restaurant3)
session.add(menuItem3)
session.commit()











print "Added menu items!"
