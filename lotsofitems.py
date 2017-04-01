from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from database_setup import Catalog, Base, CatalogItem, User

engine = create_engine('sqlite:///catalogwithuser.db')
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
User1 = User(name="Robo Barista", email="tinnyTim@udacity.com",
             picture='https://pbs.twimg.com/profile_images/2671170543/18debd694829ed78203a5a36dd364160_400x400.png')
session.add(User1)
session.commit()

# Menu for UrbanBurger
catalog1 = Catalog(user_id=1, name="Samsung")

session.add(catalog1)
session.commit()

menuItem2 = CatalogItem(user_id=1, name="Samsung Galaxy J7",
                        description="The Boost Mobile Samsung Galaxy J7 features: Android 6.0 Marshmallow OS, "
                                    "5.5 inch HD Super AMOLED Display, 13 MP Rear Camera, 5 MP Front Facing Camera, "
                                    "16 GB ROM / 2 GB ROM, 3G/4G LTE (where available), 1.4 GHz Octa-Core Processor, "
                                    "3000 mAH Battery, And Much More! Phone activation with Boost Mobile Required for "
                                    "use. Includes:Galaxy J7 handset, wall charger, USB Cable, headset and services "
                                    "guide.",
                        catalog=catalog1)

session.add(menuItem2)
session.commit()

menuItem1 = CatalogItem(user_id=1, name="Samsung J3 Nova", description="Enjoy the simplicity of Samsung smart switch "
                                                                       "which seamlessly transfers contacts, photos, "
                                                                       "music, videos, messages, notes, calendars and "
                                                                       "more to virtually any Samsung Galaxy device. "
                                                                       "Experience true and perfect color on the 5\" "
                                                                       "HD super AMOLED display featuring the most "
                                                                       "Advance version of Android Lollipop. The "
                                                                       "Samsung Nova allows you to capture life`s "
                                                                       "memories with the 5MP rear-facing camera with "
                                                                       "2MP front-facing camera. Revel with a basic "
                                                                       "smartphone for a smart life with the Samsung "
                                                                       "Nova.",
                        catalog=catalog1)

session.add(menuItem1)
session.commit()
catalog1 = Catalog(user_id=1, name="Sony")

session.add(catalog1)
session.commit()

menuItem2 = CatalogItem(user_id=1, name="Sony Xperia XZ", description="5.2\" Full HD display with premium, durable "
                                                                      "Corning Gorilla Glass 4 and polished metal in "
                                                                      "a rounded form for a comfortable fit in your "
                                                                      "hand. (Fingerprint Sensor Not Supported) 23MP "
                                                                      "camera with triple image sensors (Predictive "
                                                                      "Hybrid Autofocus, Laser Autofocus, "
                                                                      "and RGBC IR) captures your moments in motion "
                                                                      "and in true-to-life color in any condition.4K "
                                                                      "video recording with dual microphone and noise "
                                                                      "cancellation for immersive video and audio.",
                        catalog=catalog1)

session.add(menuItem2)
session.commit()

menuItem1 = CatalogItem(user_id=1, name="Sony Xperia XA", description="5\"borderless display gives you less bezel "
                                                                      "with more view Sony`s Exmor RS 13MP main "
                                                                      "camera has super-fast 0.15s Hybrid Autofocus "
                                                                      "for blur free shots Sony Exmor R 8MP "
                                                                      "front-facing camera with a wide angle lens "
                                                                      "that fits everyone in the shot 16GB onboard "
                                                                      "memory and up to 200GB expandable with MicroSD "
                                                                      "card.",
                        catalog=catalog1)

session.add(menuItem1)
session.commit()
print "added menu items!"
