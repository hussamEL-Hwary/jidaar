# -*- coding: utf-8 -*-
from sqlalchemy.sql.functions import user

from helper import session
from model import (Basic,
                   Admin,
                   Career,
                   Client,
                   Project,
                   Contact_info,
                   About)


# init database with company basic info
basic_info = Basic(mission="Jidaar is steadily and surely earning its "
                           "rank among the best in the construction industry"
                           " in Egypt. While maintaining our integrity and "
                           "enhancing our surrounding community, we retain our"
                           " clients trust by converting ordinary ventures "
                           "into extraordinary projects through our innovative"
                           " solutions. By putting our employees safety first"
                           " and empowering our team with continuous "
                           "opportunities for development, we are able to "
                           "exchange mutual benefit that facilitates growth "
                           "between Jidaar and its stakeholders, surpassing our"
                           " partners expectations and outdoing industry "
                           "standards.",
                   vision="To be one of the leading construction corporates "
                          "by innovating solutions and setting new "
                          "standards of excellence.",
                   values="Founded in 2008, Jidaar is committed to a different"
                         " philosophy: For Jidaar, our aim isnt limited to "
                         "the implementation of projects. Instead, we pursue"
                         " the art of making a house into a home, and an "
                         "office into a functional and inspiring working "
                         "space. We mastered this art by taking it upon "
                         "ourselves to determine our clients every need and "
                         "want, because we understand how crucial it is to "
                         "achieve a desired look and function for spaces not "
                         "only inside the building, but also the for the "
                         "building itself, its facilities, and other "
                         "surrounding spaces.Jidaars highly-skilled and "
                         "detail-oriented talented team are constantly "
                         "developing and in-tune with the latest methods and"
                         " technologies to acquire the skills and knowledge "
                         "necessary to tackle even the most challenging "
                         "projects, giving the company its competitive edge."
                         " Achieving success time and time again, from "
                         "factories to multinational corporates headquarters,"
                         " all in critical time-spans, we proved that we dont"
                         " believe in the word impossible. In every aspect, "
                         "Jidaar sets new standards of excellence.",
                   certification_name="cer.jpg",
                   certification_url="dummy url")
session.add(basic_info)
session.commit()
# session.close()
print "done!"


c = session.query(Basic).first()
print c.mission
print c.vision
print c.values
print c.certification_name
print c.certification_url

coco = Contact_info(address="25a, Obour buildings, Salah Salem St, Helioplis",
                    email=" info@jidaar.com",
                    mobile="01008712851",
                    fax=" 0224036646",
                    phone="0224031969")
session.add(coco)
session.commit()
abb = About(history="Jidaar Construction was established in 2008, by Arch. Hani Talha. "
                    "Utilizing the founders 30 years of technical and managerial expertise, "
                    "Jidaar managed to acquire an excellent reputation in just a few years "
                    "through working on a wide spectrum of projects, including but not limited "
                    "to: Administrative, Industrial, Residential, Recreational, and Public projects,"
                    " making Jidaar a truly multi-disciplinary practice This solid hands-on "
                    "experience enabled Jidaar to win the trust of both multinational and local "
                    "corporations, who became long-term partners of success."
                    "Empowered by its highly-skilled technical office and trained labor, "
                    "along with a strong supply-chain that provides quality materials "
                    "that are scarce in the market, Jidaar is steadily and surely earning "
                    "its rank among the best in the construction industry in Egypt.",
            iso_description="ISO 9001 is the international standard that specifies "
                            "requirements for a quality management system (QMS)."
                            "Organizations use the standard to demonstrate the ability "
                            "to consistently provide products and services that meet customer "
                            "and regulatory requirements. ISO 9001 is based on the plan-do-check-act "
                            "methodology and provides a process-oriented approach to documenting "
                            "and reviewing the structure, responsibilities,and procedures required "
                            "to achieve effective quality management in an organization.",
            iso_name="iso.jpg",
            iso_url="jjjjjh",
            ohsas_description="OHSAS 18001 sets out the minimum requirements for occupational "
                              "health and safety management best practice,it sets standards "
                              "and systems that are recognized and implemented worldwide. "
                              "OHSAS is mainly comprised ofthe policies, processes, plans, "
                              "practices, and records that define the rules governing how "
                              "Jidaar takes careof occupational health and safety, which "
                              "is one of the most important challenges facing businesses today."
                              "Jidaar puts its employees health and safety first.",
            ohsas_name="ohsas.jpg",
            ohsas_url="hjhjhjhjhj",
            code_of_conduct_name="code_of_conduct.pdf",
            code_of_conduct_url="dummy",
            brochure_name="brochure.pdf",
            brochure_url="dummy"
            )
session.add(abb)
session.commit()
session.close()


ad = Admin(user_name='boodi@jidaar.com')
ad.hash_password('RRRR123')
session.add(ad)
session.commit()

