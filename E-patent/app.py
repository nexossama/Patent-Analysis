import json
from bson import ObjectId
from flask import Flask, render_template, request, redirect, session, url_for, jsonify
from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from search import search_title
app = Flask(__name__)



docs = [
    {
    "_id": "66321b0884889bd0e1a87a7f",
    "inventor_name": [
      "Erwin Ernest Sniedzins"
    ],
    "assignee_name_orig": [
      "Individual"
    ],
    "assignee_name_current": [
      "Individual"
    ],
    "pub_date": "2013-12-10",
    "priority_date": "2013-11-07",
    "grant_date": "2013-12-10",
    "filing_date": "",
    "forward_cite_no_family": [
      {
        "patent_number": "US20120191545A1",
        "priority_date": "2010-11-25",
        "pub_date": "2012-07-26"
      },
      {
        "patent_number": "US20130262319A1",
        "priority_date": "2012-03-13",
        "pub_date": "2013-10-03"
      },
      {
        "patent_number": "US20140180677A1",
        "priority_date": "2012-11-21",
        "pub_date": "2014-06-26"
      },
      {
        "patent_number": "US20140272908A1",
        "priority_date": "2013-03-15",
        "pub_date": "2014-09-18"
      },
      {
        "patent_number": "US20140324541A1",
        "priority_date": "2013-04-30",
        "pub_date": "2014-10-30"
      },
      {
        "patent_number": "US20150178258A1",
        "priority_date": "2012-05-02",
        "pub_date": "2015-06-25"
      },
      {
        "patent_number": "US20150339326A1",
        "priority_date": "2014-05-22",
        "pub_date": "2015-11-26"
      },
      {
        "patent_number": "US20160148524A1",
        "priority_date": "2014-11-21",
        "pub_date": "2016-05-26"
      },
      {
        "patent_number": "US20160232245A1",
        "priority_date": "2015-02-10",
        "pub_date": "2016-08-11"
      },
      {
        "patent_number": "US20160253914A1",
        "priority_date": "2011-12-19",
        "pub_date": "2016-09-01"
      },
      {
        "patent_number": "US20160328380A1",
        "priority_date": "2014-02-22",
        "pub_date": "2016-11-10"
      },
      {
        "patent_number": "US9646266B2",
        "priority_date": "2012-10-22",
        "pub_date": "2017-05-09"
      },
      {
        "patent_number": "CN107016630A",
        "priority_date": "2017-02-09",
        "pub_date": "2017-08-04"
      },
      {
        "patent_number": "US9779756B2",
        "priority_date": "2015-12-11",
        "pub_date": "2017-10-03"
      },
      {
        "patent_number": "WO2017192851A1",
        "priority_date": "2016-05-04",
        "pub_date": "2017-11-09"
      },
      {
        "patent_number": "US20180225981A1",
        "priority_date": "2017-02-03",
        "pub_date": "2018-08-09"
      },
      {
        "patent_number": "US10108601B2",
        "priority_date": "2013-09-19",
        "pub_date": "2018-10-23"
      },
      {
        "patent_number": "US10166478B2",
        "priority_date": "2015-09-30",
        "pub_date": "2019-01-01"
      },
      {
        "patent_number": "US10497272B2",
        "priority_date": "2016-11-23",
        "pub_date": "2019-12-03"
      },
      {
        "patent_number": "US10592603B2",
        "priority_date": "2016-02-03",
        "pub_date": "2020-03-17"
      },
      {
        "patent_number": "WO2020161731A1",
        "priority_date": "2019-02-06",
        "pub_date": "2020-08-13"
      },
      {
        "patent_number": "US10777090B2",
        "priority_date": "2015-04-10",
        "pub_date": "2020-09-15"
      },
      {
        "patent_number": "US10854101B1",
        "priority_date": "2016-03-09",
        "pub_date": "2020-12-01"
      },
      {
        "patent_number": "US10915819B2",
        "priority_date": "2016-07-01",
        "pub_date": "2021-02-09"
      },
      {
        "patent_number": "US11022511B2",
        "priority_date": "2018-04-18",
        "pub_date": "2021-06-01"
      },
      {
        "patent_number": "US11042702B2",
        "priority_date": "2016-02-04",
        "pub_date": "2021-06-22"
      },
      {
        "patent_number": "US11069250B2",
        "priority_date": "2016-11-23",
        "pub_date": "2021-07-20"
      },
      {
        "patent_number": "US11144810B2",
        "priority_date": "2017-06-27",
        "pub_date": "2021-10-12"
      },
      {
        "patent_number": "US11232798B2",
        "priority_date": "2020-05-21",
        "pub_date": "2022-01-25"
      },
      {
        "patent_number": "US11404051B2",
        "priority_date": "2020-05-21",
        "pub_date": "2022-08-02"
      },
      {
        "patent_number": "US20220261546A1",
        "priority_date": "2020-09-04",
        "pub_date": "2022-08-18"
      },
      {
        "patent_number": "US11491399B2",
        "priority_date": "2020-04-28",
        "pub_date": "2022-11-08"
      },
      {
        "patent_number": "CN116596719A",
        "priority_date": "2023-07-18",
        "pub_date": "2023-08-15"
      },
      {
        "patent_number": "CN117271710A",
        "priority_date": "2023-11-17",
        "pub_date": "2023-12-22"
      }
    ],
    "forward_cite_yes_family": [
      {
        "patent_number": "WO2013016719A1",
        "priority_date": "2011-07-28",
        "pub_date": "2013-01-31"
      },
      {
        "patent_number": "US20130157245A1",
        "priority_date": "2011-12-15",
        "pub_date": "2013-06-20"
      },
      {
        "patent_number": "JP2013246384A",
        "priority_date": "2012-05-29",
        "pub_date": "2013-12-09"
      },
      {
        "patent_number": "US20140006000A1",
        "priority_date": "2012-07-02",
        "pub_date": "2014-01-02"
      },
      {
        "patent_number": "US20140156782A1",
        "priority_date": "2012-11-30",
        "pub_date": "2014-06-05"
      },
      {
        "patent_number": "CN104866607B",
        "priority_date": "2015-06-04",
        "pub_date": "2018-01-12"
      },
      {
        "patent_number": "WO2017018940A1",
        "priority_date": "2015-07-27",
        "pub_date": "2017-02-02"
      },
      {
        "patent_number": "CN108367081A",
        "priority_date": "2015-10-14",
        "pub_date": "2018-08-03"
      },
      {
        "patent_number": "US20180033325A1",
        "priority_date": "2016-07-29",
        "pub_date": "2018-02-01"
      },
      {
        "patent_number": "US20180032524A1",
        "priority_date": "2016-07-29",
        "pub_date": "2018-02-01"
      },
      {
        "patent_number": "US20180197423A1",
        "priority_date": "2017-01-12",
        "pub_date": "2018-07-12"
      },
      {
        "patent_number": "CN106960042A",
        "priority_date": "2017-03-29",
        "pub_date": "2017-07-18"
      },
      {
        "patent_number": "CN107230401A",
        "priority_date": "2017-06-02",
        "pub_date": "2017-10-03"
      },
      {
        "patent_number": "WO2019173737A1",
        "priority_date": "2018-03-08",
        "pub_date": "2019-09-12"
      },
      {
        "patent_number": "US20210327292A1",
        "priority_date": "2018-10-02",
        "pub_date": "2021-10-21"
      },
      {
        "patent_number": "US20210192973A1",
        "priority_date": "2019-12-19",
        "pub_date": "2021-06-24"
      },
      {
        "patent_number": "US11501655B2",
        "priority_date": "2020-07-15",
        "pub_date": "2022-11-15"
      }
    ],
    "backward_cite_no_family": [
      {
        "patent_number": "US6212358B1",
        "priority_date": "1996-07-02",
        "pub_date": "2001-04-03"
      },
      {
        "patent_number": "US20040161734A1",
        "priority_date": "2000-04-24",
        "pub_date": "2004-08-19"
      },
      {
        "patent_number": "US20020049634A1",
        "priority_date": "2000-07-06",
        "pub_date": "2002-04-25"
      },
      {
        "patent_number": "US6622003B1",
        "priority_date": "2000-08-14",
        "pub_date": "2003-09-16"
      },
      {
        "patent_number": "US20020087560A1",
        "priority_date": "2000-12-29",
        "pub_date": "2002-07-04"
      },
      {
        "patent_number": "US20020188583A1",
        "priority_date": "2001-05-25",
        "pub_date": "2002-12-12"
      },
      {
        "patent_number": "US20030163784A1",
        "priority_date": "2001-12-12",
        "pub_date": "2003-08-28"
      },
      {
        "patent_number": "US20040024776A1",
        "priority_date": "2002-07-30",
        "pub_date": "2004-02-05"
      },
      {
        "patent_number": "US20040110119A1",
        "priority_date": "2002-09-03",
        "pub_date": "2004-06-10"
      },
      {
        "patent_number": "US20060136409A1",
        "priority_date": "2004-12-17",
        "pub_date": "2006-06-22"
      },
      {
        "patent_number": "US20070111182A1",
        "priority_date": "2005-10-26",
        "pub_date": "2007-05-17"
      },
      {
        "patent_number": "US20070179776A1",
        "priority_date": "2006-01-27",
        "pub_date": "2007-08-02"
      }
    ],
    "backward_cite_yes_family": [
      {
        "patent_number": "US6130968A",
        "priority_date": "1997-10-03",
        "pub_date": "2000-10-10"
      },
      {
        "patent_number": "GB9726654D0",
        "priority_date": "1997-12-17",
        "pub_date": "1998-02-18"
      },
      {
        "patent_number": "US20050216251A1",
        "priority_date": "2004-03-24",
        "pub_date": "2005-09-29"
      },
      {
        "patent_number": "US20070269775A1",
        "priority_date": "2004-09-14",
        "pub_date": "2007-11-22"
      }
    ],
    "abstract_text": "The real time learning system and method provides a self learning environment to learn language or subjects faster and easier using textual content obtained in real time. The system is a computer-aided and management educational system that includes a real-time content processing module, a learning management Module, a content management database, an exercise generator module with Dictionaries, Picture Media, Music Libraries, Life Management and a User block. The system transforms any Real Time textual information into learning content and implements user learning exercises. Learning exercises are automatically created as multiple choice tests, filling blanks, quizzes, puzzles, crosswords, etc. from this learning content in real-time, based on a teacher or student online request for information. Linguistic text processing, keyword extraction and semantic procedures allow extraction of text information with a different data set to generate more intellectual exercises as comprehension tests, writing and grammar exercises. Different learning technologies are used to generate exercise implementation as visual mnemonics for remembering (Syntality 1 ), interactive templates, games, multi-sensor activities. A Life Management module includes a Personal Action Success Strategy (PASS) System that contains Time Management, Motivation and Goal Setting Systems.",
    "country": "United States",
    "code": "US8602793B1",
    "title": "Real time learning and self improvement educational system and method",
    "link": "https://patents.google.com/patent/US8602793B1/en",
    "source": "google patent",
    "applicants": [
      "Individual"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a80",
    "inventor_name": [
      "Erwin E. Sniedzins"
    ],
    "assignee_name_orig": [
      "Individual"
    ],
    "assignee_name_current": [
      "Individual"
    ],
    "pub_date": "2013-01-15",
    "priority_date": "",
    "grant_date": "",
    "filing_date": "",
    "forward_cite_no_family": [
      {
        "patent_number": "US9330164B1",
        "priority_date": "2012-10-26",
        "pub_date": "2016-05-03"
      }
    ],
    "forward_cite_yes_family": [],
    "backward_cite_no_family": [],
    "backward_cite_yes_family": [],
    "abstract_text": "The real time learning system and method provides a self learning environment to learn language or subjects faster and easier using textual content obtained in real time. The system is a computer-aided and management educational system that includes a real-time content processing module, a learning management Module, a content management database, an exercise generator module with Dictionaries, Picture Media, Music Libraries, Life Management and a User block. The system transforms any Real Time textual information into learning content and implements user learing exercises. Learning exercises are automatically created as multiple choice tests, filling blanks, quizzes, puzzles, crosswords, etc. from this learing content in real-time, based on a teacher or student online request for information.  Linguistic text processing, keyword extraction and semantic procedures allow extraction of text information with a different data set to generate more intellectual exercises as comprehension tests, writing and grammar exercises. Different learning technologies are used to generate exercise implementation as visual mnemonics for remembering (Syntality1), interactive templates, games, multi-sensor activities. A Life Management module includes a Personal Action Success Strategy (PASS) System that contains Time Management, Motivation and Goal Setting Systems.",
    "country": "Canada",
    "code": "CA2752107A1",
    "title": "Real time learning and self improvement educational system and method",
    "link": "https://patents.google.com/patent/CA2752107A1/en",
    "source": "google patent",
    "applicants": [
      "Priority claimed from US13/183",
      "945"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a81",
    "inventor_name": [
      "Erwin E. Sniedzins"
    ],
    "assignee_name_orig": [
      "Individual"
    ],
    "assignee_name_current": [
      "Individual"
    ],
    "pub_date": "2013-01-15",
    "priority_date": "",
    "grant_date": "",
    "filing_date": "",
    "forward_cite_no_family": [
      {
        "patent_number": "US9330164B1",
        "priority_date": "2012-10-26",
        "pub_date": "2016-05-03"
      }
    ],
    "forward_cite_yes_family": [],
    "backward_cite_no_family": [],
    "backward_cite_yes_family": [],
    "abstract_text": "The real time learning system and method provides a self learning environment to learn language or subjects faster and easier using textual content obtained in real time. The system is a computer-aided and management educational system that includes a real-time content processing module, a learning management Module, a content management database, an exercise generator module with Dictionaries, Picture Media, Music Libraries, Life Management and a User block. The system transforms any Real Time textual information into learning content and implements user learing exercises. Learning exercises are automatically created as multiple choice tests, filling blanks, quizzes, puzzles, crosswords, etc. from this learing content in real-time, based on a teacher or student online request for information.  Linguistic text processing, keyword extraction and semantic procedures allow extraction of text information with a different data set to generate more intellectual exercises as comprehension tests, writing and grammar exercises. Different learning technologies are used to generate exercise implementation as visual mnemonics for remembering (Syntality1), interactive templates, games, multi-sensor activities. A Life Management module includes a Personal Action Success Strategy (PASS) System that contains Time Management, Motivation and Goal Setting Systems.",
    "country": "Canada",
    "code": "CA2752107A1",
    "title": "Real time learning and self improvement educational system and method",
    "link": "https://patents.google.com/patent/CA2752107A1/en",
    "source": "google patent",
    "applicants": [
      "Priority claimed from US13/183",
      "945"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a82",
    "inventor_name": [
      "박호성",
      "최대선"
    ],
    "assignee_name_orig": [
      "공주대학교 산학협력단"
    ],
    "assignee_name_current": [],
    "pub_date": "2021-05-20",
    "priority_date": "",
    "grant_date": "",
    "filing_date": "",
    "forward_cite_no_family": [],
    "forward_cite_yes_family": [
      {
        "patent_number": "KR102592935B1",
        "priority_date": "2020-12-22",
        "pub_date": "2023-10-23"
      }
    ],
    "backward_cite_no_family": [
      {
        "patent_number": "KR20160095856A",
        "priority_date": "2015-02-04",
        "pub_date": "2016-08-12"
      },
      {
        "patent_number": "KR20190061446A",
        "priority_date": "2017-11-28",
        "pub_date": "2019-06-05"
      },
      {
        "patent_number": "KR20190094068A",
        "priority_date": "2018-01-11",
        "pub_date": "2019-08-12"
      }
    ],
    "backward_cite_yes_family": [],
    "abstract_text": "The present invention relates to an apparatus and method for retraining a substitute model for an evasion attack, and an evasion attack apparatus. The present invention is characterized in: on the basis of a substitute model previously trained in the same type as a target model trained, via a neural network, to classify labels of input data, generating, from original data, specific attack data for allowing the target model to misclassify labels of the original data to input, to the target model, the generated specific attack data as a query for the target model; acquiring a classification result obtained by classifying, by the target model, labels of the specific attack data in response to the query; and on the basis of the acquired classification result and the specific attack data, retraining the substitute model so that the substitute model partially imitates the target model.",
    "country": "World Intellectual Property Organization (WIPO)",
    "code": "WO2021095984A1",
    "title": "Apparatus and method for retraining substitute model for evasion attack, and evasion attack apparatus",
    "link": "https://patents.google.com/patent/WO2021095984A1/en",
    "source": "google patent",
    "applicants": [
      "공주대학교 산학협력단"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a83",
    "inventor_name": [
      "邹赛",
      "李林",
      "聂强",
      "胡幻",
      "李法平",
      "肖山"
    ],
    "assignee_name_orig": [
      "Chongqing College of Electronic Engineering"
    ],
    "assignee_name_current": [
      "Chongqing College of Electronic Engineering"
    ],
    "pub_date": "2021-04-20",
    "priority_date": "2021-01-11",
    "grant_date": "",
    "filing_date": "",
    "forward_cite_no_family": [
      {
        "patent_number": "CN113470448A",
        "priority_date": "2021-06-30",
        "pub_date": "2021-10-01"
      },
      {
        "patent_number": "CN113487213A",
        "priority_date": "2021-07-20",
        "pub_date": "2021-10-08"
      },
      {
        "patent_number": "CN114117054A",
        "priority_date": "2022-01-24",
        "pub_date": "2022-03-01"
      },
      {
        "patent_number": "CN114493094A",
        "priority_date": "2021-12-15",
        "pub_date": "2022-05-13"
      },
      {
        "patent_number": "CN115480923A",
        "priority_date": "2022-10-10",
        "pub_date": "2022-12-16"
      },
      {
        "patent_number": "CN116523225A",
        "priority_date": "2023-04-18",
        "pub_date": "2023-08-01"
      }
    ],
    "forward_cite_yes_family": [],
    "backward_cite_no_family": [
      {
        "patent_number": "JP2007133078A",
        "priority_date": "2005-11-09",
        "pub_date": "2007-05-31"
      },
      {
        "patent_number": "CN106203811A",
        "priority_date": "2016-07-05",
        "pub_date": "2016-12-07"
      },
      {
        "patent_number": "CN107169903A",
        "priority_date": "2017-07-25",
        "pub_date": "2017-09-15"
      },
      {
        "patent_number": "CN108182489A",
        "priority_date": "2017-12-25",
        "pub_date": "2018-06-19"
      },
      {
        "patent_number": "CN111914162A",
        "priority_date": "2020-06-01",
        "pub_date": "2020-11-10"
      }
    ],
    "backward_cite_yes_family": [],
    "abstract_text": "The invention provides an intelligent evaluation method for classroom teaching effects of colleges and universities, which comprises the following steps of S1 obtaining various dynamic data of classroom teaching of colleges and universities and establishing a prior probability model; s2, establishing an intelligent dynamic evaluation model of classroom teaching effects in colleges and universities; s3, combining the prior probability model in the step S1 and the intelligent dynamic evaluation model in the step S2, establishing an intelligent feedback system, and pushing a customized culture scheme by taking the personalized data of students as a basis. By means of the fusion innovation of an artificial intelligence technology, a VR technology, a data calculation technology, a 5G technology and an Internet of things technology, the evaluation data is comprehensive, the indexes of an evaluation system can be quantized, the evaluation result is diversified, the education evaluation is promoted to enter a new development stage, and an intelligent new trend is reflected or the education is made to return to essence.",
    "country": "China",
    "code": "CN112686789A",
    "title": "Intelligent evaluation method for classroom teaching effect of colleges and universities",
    "link": "https://patents.google.com/patent/CN112686789A/en",
    "source": "google patent",
    "applicants": [
      "Chongqing College of Electronic Engineering"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a84",
    "inventor_name": [
      "Hetal B. Kurani"
    ],
    "assignee_name_orig": [
      "Individual"
    ],
    "assignee_name_current": [
      "Individual"
    ],
    "pub_date": "2020-08-13",
    "priority_date": "2019-02-11",
    "grant_date": "",
    "filing_date": "",
    "forward_cite_no_family": [
      {
        "patent_number": "US20200364492A1",
        "priority_date": "2019-05-15",
        "pub_date": "2020-11-19"
      },
      {
        "patent_number": "CN112784895A",
        "priority_date": "2021-01-18",
        "pub_date": "2021-05-11"
      },
      {
        "patent_number": "US11120700B2",
        "priority_date": "2019-04-11",
        "pub_date": "2021-09-14"
      },
      {
        "patent_number": "US20210375149A1",
        "priority_date": "2020-06-02",
        "pub_date": "2021-12-02"
      },
      {
        "patent_number": "US20220005368A1",
        "priority_date": "2020-07-01",
        "pub_date": "2022-01-06"
      },
      {
        "patent_number": "WO2022147359A1",
        "priority_date": "2020-12-31",
        "pub_date": "2022-07-07"
      },
      {
        "patent_number": "CN116739858A",
        "priority_date": "2023-08-15",
        "pub_date": "2023-09-12"
      },
      {
        "patent_number": "WO2023241976A1",
        "priority_date": "2022-06-14",
        "pub_date": "2023-12-21"
      }
    ],
    "forward_cite_yes_family": [],
    "backward_cite_no_family": [],
    "backward_cite_yes_family": [],
    "abstract_text": "A personalized and adaptive automated math learning system and method based on personal attributes, structured prediction, and reinforcement learning is disclosed. The personalization is achieved by data mining the personal attributes and creating competency clusters. The lesson plan and course is designed based on learners' competency levels to teach the subject matter in the shortest possible time. The adaptive automated machine learning method can change teaching methods and formats to become more interactive. After completion of the course, learners are expected to achieve expert competency.",
    "country": "United States",
    "code": "US20200258420A1",
    "title": "Personalized and adaptive math learning system",
    "link": "https://patents.google.com/patent/US20200258420A1/en",
    "source": "google patent",
    "applicants": [
      "Individual"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a85",
    "inventor_name": [
      "Sooyoung Kim",
      "Shinnyue KANG"
    ],
    "assignee_name_orig": [
      "LG Electronics Inc"
    ],
    "assignee_name_current": [
      "LG Electronics Inc"
    ],
    "pub_date": "2018-10-18",
    "priority_date": "",
    "grant_date": "2019-10-08",
    "filing_date": "",
    "forward_cite_no_family": [
      {
        "patent_number": "US20200128159A1",
        "priority_date": "2018-10-19",
        "pub_date": "2020-04-23"
      },
      {
        "patent_number": "US10951813B2",
        "priority_date": "2017-12-01",
        "pub_date": "2021-03-16"
      }
    ],
    "forward_cite_yes_family": [
      {
        "patent_number": "WO2016024440A1",
        "priority_date": "2014-08-12",
        "pub_date": "2016-02-18"
      },
      {
        "patent_number": "CN110769149B",
        "priority_date": "2015-04-23",
        "pub_date": "2021-05-11"
      },
      {
        "patent_number": "US9912860B2",
        "priority_date": "2016-06-12",
        "pub_date": "2018-03-06"
      },
      {
        "patent_number": "DK180859B1",
        "priority_date": "2017-06-04",
        "pub_date": "2022-05-23"
      },
      {
        "patent_number": "US11112964B2",
        "priority_date": "2018-02-09",
        "pub_date": "2021-09-07"
      },
      {
        "patent_number": "US11722764B2",
        "priority_date": "2018-05-07",
        "pub_date": "2023-08-08"
      },
      {
        "patent_number": "US10375313B1",
        "priority_date": "2018-05-07",
        "pub_date": "2019-08-06"
      },
      {
        "patent_number": "DK201870623A1",
        "priority_date": "2018-09-11",
        "pub_date": "2020-04-15"
      },
      {
        "patent_number": "US10674072B1",
        "priority_date": "2019-05-06",
        "pub_date": "2020-06-02"
      },
      {
        "patent_number": "US11770601B2",
        "priority_date": "2019-05-06",
        "pub_date": "2023-09-26"
      },
      {
        "patent_number": "US11321857B2",
        "priority_date": "2018-09-28",
        "pub_date": "2022-05-03"
      },
      {
        "patent_number": "US11128792B2",
        "priority_date": "2018-09-28",
        "pub_date": "2021-09-21"
      },
      {
        "patent_number": "US11159731B2",
        "priority_date": "2019-02-19",
        "pub_date": "2021-10-26"
      },
      {
        "patent_number": "CN111901479B",
        "priority_date": "2019-05-06",
        "pub_date": "2021-05-25"
      },
      {
        "patent_number": "US11706521B2",
        "priority_date": "2019-05-06",
        "pub_date": "2023-07-18"
      },
      {
        "patent_number": "US11611714B2",
        "priority_date": "2019-08-01",
        "pub_date": "2023-03-21"
      },
      {
        "patent_number": "US11849264B2",
        "priority_date": "2019-11-22",
        "pub_date": "2023-12-19"
      },
      {
        "patent_number": "JP7359283B2",
        "priority_date": "2020-02-10",
        "pub_date": "2023-10-11"
      },
      {
        "patent_number": "US11039074B1",
        "priority_date": "2020-06-01",
        "pub_date": "2021-06-15"
      },
      {
        "patent_number": "US11212449B1",
        "priority_date": "2020-09-25",
        "pub_date": "2021-12-28"
      },
      {
        "patent_number": "KR20220054003A",
        "priority_date": "2020-10-23",
        "pub_date": "2022-05-02"
      },
      {
        "patent_number": "WO2022119109A1",
        "priority_date": "2020-12-04",
        "pub_date": "2022-06-09"
      },
      {
        "patent_number": "US11671696B2",
        "priority_date": "2021-04-19",
        "pub_date": "2023-06-06"
      },
      {
        "patent_number": "US11539876B2",
        "priority_date": "2021-04-30",
        "pub_date": "2022-12-27"
      },
      {
        "patent_number": "US11778339B2",
        "priority_date": "2021-04-30",
        "pub_date": "2023-10-03"
      },
      {
        "patent_number": "WO2023090747A1",
        "priority_date": "2021-11-17",
        "pub_date": "2023-05-25"
      }
    ],
    "backward_cite_no_family": [
      {
        "patent_number": "US6919927B1",
        "priority_date": "1998-06-05",
        "pub_date": "2005-07-19"
      },
      {
        "patent_number": "US20060055814A1",
        "priority_date": "2004-09-16",
        "pub_date": "2006-03-16"
      },
      {
        "patent_number": "US20070002016A1",
        "priority_date": "2005-06-29",
        "pub_date": "2007-01-04"
      },
      {
        "patent_number": "US8390686B2",
        "priority_date": "2005-09-20",
        "pub_date": "2013-03-05"
      },
      {
        "patent_number": "US9521313B2",
        "priority_date": "2012-08-07",
        "pub_date": "2016-12-13"
      },
      {
        "patent_number": "US20140362257A1",
        "priority_date": "2013-06-11",
        "pub_date": "2014-12-11"
      },
      {
        "patent_number": "US20160202852A1",
        "priority_date": "2013-08-22",
        "pub_date": "2016-07-14"
      },
      {
        "patent_number": "US20160255268A1",
        "priority_date": "2014-09-05",
        "pub_date": "2016-09-01"
      }
    ],
    "backward_cite_yes_family": [
      {
        "patent_number": "US9827250B2",
        "priority_date": "2012-07-31",
        "pub_date": "2017-11-28"
      },
      {
        "patent_number": "JP6496995B2",
        "priority_date": "2014-07-28",
        "pub_date": "2019-04-10"
      }
    ],
    "abstract_text": "A mobile terminal includes a camera configured to acquire a preview image, a display configured to display the acquired preview image, an artificial intelligence unit configured to sense photographing state information of the preview image, to recognize a direction of a user's hand gripping the mobile terminal according to the sensed photographing state information, and to display a floating button on the display at a position corresponding to the recognized direction of the user's hand, and a controller configured to perform a function corresponding to the floating button selected according to a request for selecting the floating button. The artificial intelligence unit may change attributes of the floating button according to sensing of additional photographing state information after displaying the floating button.",
    "country": "United States",
    "code": "US10440275B2",
    "title": "Mobile terminal displaying a continuous-photographing button or a moving-image floating button",
    "link": "https://patents.google.com/patent/US10440275B2/en",
    "source": "google patent",
    "applicants": [
      "LG Electronics Inc"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a86",
    "inventor_name": [
      "Yu Inoue",
      "Masahiro Kazama",
      "Isao Nishizawa"
    ],
    "assignee_name_orig": [
      "Kitz Corp"
    ],
    "assignee_name_current": [
      "Kitz Corp"
    ],
    "pub_date": "2021-03-22",
    "priority_date": "",
    "grant_date": "2022-07-07",
    "filing_date": "",
    "forward_cite_no_family": [],
    "forward_cite_yes_family": [
      {
        "patent_number": "JP7124273B2",
        "priority_date": "2017-07-21",
        "pub_date": "2022-08-24"
      },
      {
        "patent_number": "JP7124275B2",
        "priority_date": "2017-07-21",
        "pub_date": "2022-08-24"
      },
      {
        "patent_number": "JP7124272B2",
        "priority_date": "2017-07-21",
        "pub_date": "2022-08-24"
      },
      {
        "patent_number": "JP7124271B2",
        "priority_date": "2017-07-21",
        "pub_date": "2022-08-24"
      },
      {
        "patent_number": "US11134832B2",
        "priority_date": "2019-06-20",
        "pub_date": "2021-10-05"
      },
      {
        "patent_number": "JP2021111207A",
        "priority_date": "2020-01-14",
        "pub_date": "2021-08-02"
      },
      {
        "patent_number": "JP2021124981A",
        "priority_date": "2020-02-05",
        "pub_date": "2021-08-30"
      },
      {
        "patent_number": "JP6779456B1",
        "priority_date": "2020-03-16",
        "pub_date": "2020-11-04"
      },
      {
        "patent_number": "JP6783486B1",
        "priority_date": "2020-03-17",
        "pub_date": "2020-11-11"
      },
      {
        "patent_number": "JP6783488B1",
        "priority_date": "2020-03-27",
        "pub_date": "2020-11-11"
      },
      {
        "patent_number": "JP7320473B2",
        "priority_date": "2020-03-27",
        "pub_date": "2023-08-03"
      },
      {
        "patent_number": "JP6783489B1",
        "priority_date": "2020-03-27",
        "pub_date": "2020-11-11"
      },
      {
        "patent_number": "JP6779457B1",
        "priority_date": "2020-04-15",
        "pub_date": "2020-11-04"
      },
      {
        "patent_number": "JP6779458B1",
        "priority_date": "2020-04-28",
        "pub_date": "2020-11-04"
      },
      {
        "patent_number": "JP6779459B1",
        "priority_date": "2020-04-28",
        "pub_date": "2020-11-04"
      },
      {
        "patent_number": "JP7093031B2",
        "priority_date": "2020-09-23",
        "pub_date": "2022-06-29"
      },
      {
        "patent_number": "CN112197056B",
        "priority_date": "2020-10-19",
        "pub_date": "2021-07-20"
      },
      {
        "patent_number": "JP7058447B1",
        "priority_date": "2020-11-30",
        "pub_date": "2022-04-22"
      },
      {
        "patent_number": "JP2022093261A",
        "priority_date": "2020-12-11",
        "pub_date": "2022-06-23"
      },
      {
        "patent_number": "WO2022260164A1",
        "priority_date": "2021-06-10",
        "pub_date": "2022-12-15"
      },
      {
        "patent_number": "DE102021205838A1",
        "priority_date": "2021-06-10",
        "pub_date": "2022-12-15"
      },
      {
        "patent_number": "CN114383836B",
        "priority_date": "2021-12-09",
        "pub_date": "2023-12-08"
      },
      {
        "patent_number": "CN114263750B",
        "priority_date": "2021-12-21",
        "pub_date": "2023-05-19"
      },
      {
        "patent_number": "CN114508389B",
        "priority_date": "2021-12-29",
        "pub_date": "2024-02-13"
      },
      {
        "patent_number": "JP2023104150A",
        "priority_date": "2022-01-17",
        "pub_date": "2023-07-28"
      },
      {
        "patent_number": "WO2023210694A1",
        "priority_date": "2022-04-28",
        "pub_date": "2023-11-02"
      },
      {
        "patent_number": "JP7374528B1",
        "priority_date": "2022-10-17",
        "pub_date": "2023-11-07"
      },
      {
        "patent_number": "KR102570319B1",
        "priority_date": "2023-06-01",
        "pub_date": "2023-08-25"
      }
    ],
    "backward_cite_no_family": [],
    "backward_cite_yes_family": [
      {
        "patent_number": "JPS4990338U",
        "priority_date": "1972-11-27",
        "pub_date": "1974-08-06"
      },
      {
        "patent_number": "US5487302A",
        "priority_date": "1993-03-01",
        "pub_date": "1996-01-30"
      },
      {
        "patent_number": "US5887608A",
        "priority_date": "1995-06-21",
        "pub_date": "1999-03-30"
      },
      {
        "patent_number": "JP4073902B2",
        "priority_date": "2004-09-15",
        "pub_date": "2008-04-09"
      },
      {
        "patent_number": "US20060146469A1",
        "priority_date": "2004-11-08",
        "pub_date": "2006-07-06"
      },
      {
        "patent_number": "US7478012B2",
        "priority_date": "2006-06-30",
        "pub_date": "2009-01-13"
      },
      {
        "patent_number": "US7886766B2",
        "priority_date": "2006-12-27",
        "pub_date": "2011-02-15"
      },
      {
        "patent_number": "DE102008064359A1",
        "priority_date": "2008-12-22",
        "pub_date": "2010-07-01"
      },
      {
        "patent_number": "DE102009022891B3",
        "priority_date": "2009-05-27",
        "pub_date": "2010-11-18"
      },
      {
        "patent_number": "US20110083746A1",
        "priority_date": "2009-10-09",
        "pub_date": "2011-04-14"
      },
      {
        "patent_number": "JP4990338B2",
        "priority_date": "2009-10-13",
        "pub_date": "2012-08-01"
      },
      {
        "patent_number": "TWI531740B",
        "priority_date": "2010-03-31",
        "pub_date": "2016-05-01"
      },
      {
        "patent_number": "JP5779946B2",
        "priority_date": "2011-04-07",
        "pub_date": "2015-09-16"
      },
      {
        "patent_number": "JP4843111B1",
        "priority_date": "2011-05-18",
        "pub_date": "2011-12-21"
      },
      {
        "patent_number": "KR20190022899A",
        "priority_date": "2011-07-21",
        "pub_date": "2019-03-06"
      },
      {
        "patent_number": "EP2859261A4",
        "priority_date": "2012-06-07",
        "pub_date": "2016-01-20"
      },
      {
        "patent_number": "WO2013191736A1",
        "priority_date": "2012-06-18",
        "pub_date": "2013-12-27"
      },
      {
        "patent_number": "US10718727B2",
        "priority_date": "2013-03-14",
        "pub_date": "2020-07-21"
      },
      {
        "patent_number": "IL227260A",
        "priority_date": "2013-06-30",
        "pub_date": "2017-01-31"
      },
      {
        "patent_number": "JP6221652B2",
        "priority_date": "2013-11-08",
        "pub_date": "2017-11-01"
      },
      {
        "patent_number": "CN204284634U",
        "priority_date": "2014-11-03",
        "pub_date": "2015-04-22"
      },
      {
        "patent_number": "ES2809553T3",
        "priority_date": "2015-03-02",
        "pub_date": "2021-03-04"
      },
      {
        "patent_number": "WO2016175800A1",
        "priority_date": "2015-04-29",
        "pub_date": "2016-11-03"
      },
      {
        "patent_number": "CN204922194U",
        "priority_date": "2015-05-22",
        "pub_date": "2015-12-30"
      },
      {
        "patent_number": "JP2017194122A",
        "priority_date": "2016-04-21",
        "pub_date": "2017-10-26"
      },
      {
        "patent_number": "US9934671B1",
        "priority_date": "2016-10-24",
        "pub_date": "2018-04-03"
      },
      {
        "patent_number": "US10619760B2",
        "priority_date": "2016-10-24",
        "pub_date": "2020-04-14"
      }
    ],
    "abstract_text": "",
    "country": "Spain",
    "code": "ES2813248B2",
    "title": "Valve status detection method and valve status detection system",
    "link": "https://patents.google.com/patent/ES2813248B2/en",
    "source": "google patent",
    "applicants": [
      "Kitz Corp"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a87",
    "inventor_name": [
      "郑平平",
      "周云",
      "石兴碌",
      "刘清彪",
      "刘晓"
    ],
    "assignee_name_orig": [
      "Beijing Aixuexi Bole Education Technology Co ltd"
    ],
    "assignee_name_current": [
      "Beijing Aixuexi Bole Education Technology Co ltd"
    ],
    "pub_date": "2021-10-19",
    "priority_date": "2021-07-27",
    "grant_date": "",
    "filing_date": "",
    "forward_cite_no_family": [
      {
        "patent_number": "CN114302168A",
        "priority_date": "2021-11-25",
        "pub_date": "2022-04-08"
      },
      {
        "patent_number": "CN114363322A",
        "priority_date": "2022-01-05",
        "pub_date": "2022-04-15"
      },
      {
        "patent_number": "CN115129895A",
        "priority_date": "2022-07-05",
        "pub_date": "2022-09-30"
      },
      {
        "patent_number": "CN115599997A",
        "priority_date": "2022-10-13",
        "pub_date": "2023-01-13"
      },
      {
        "patent_number": "CN116127172A",
        "priority_date": "2023-02-16",
        "pub_date": "2023-05-16"
      },
      {
        "patent_number": "CN116308935A",
        "priority_date": "2023-05-19",
        "pub_date": "2023-06-23"
      },
      {
        "patent_number": "CN117390522A",
        "priority_date": "2023-12-12",
        "pub_date": "2024-01-12"
      },
      {
        "patent_number": "CN117473076B",
        "priority_date": "2023-12-27",
        "pub_date": "2024-03-08"
      }
    ],
    "forward_cite_yes_family": [],
    "backward_cite_no_family": [
      {
        "patent_number": "CN107038508A",
        "priority_date": "2017-06-06",
        "pub_date": "2017-08-11"
      },
      {
        "patent_number": "CN110109963A",
        "priority_date": "2017-12-31",
        "pub_date": "2019-08-09"
      },
      {
        "patent_number": "CN109858797A",
        "priority_date": "2019-01-25",
        "pub_date": "2019-06-07"
      },
      {
        "patent_number": "CN111445362A",
        "priority_date": "2020-03-23",
        "pub_date": "2020-07-24"
      },
      {
        "patent_number": "CN112016767A",
        "priority_date": "2020-10-09",
        "pub_date": "2020-12-01"
      },
      {
        "patent_number": "CN112613736A",
        "priority_date": "2020-12-23",
        "pub_date": "2021-04-06"
      }
    ],
    "backward_cite_yes_family": [],
    "abstract_text": "The invention provides a self-adaptive learning system based on big data and deep learning and a construction method thereof. The system comprises: the student module is used for automatically recording the learning process, the learning behavior and the learning result of the learner; the intelligent analysis module is used for analyzing learning behaviors according to the recorded learner learning data and the decomposed micro knowledge particles in the knowledge domain model, automatically evaluating the initial level, the learning target requirement and the learning performance of the learner and forming a related knowledge map; and the resource module is used for feeding back the formed knowledge map and learning evaluation to the learning recommendation system, and automatically recommending relevant learning content, learning resources and learning paths which are interested by the learner. The self-adaptive learning system based on big data and deep learning and the construction method thereof provided by the invention can realize the purposes of individual and autonomous learning of students, accurate teaching of teachers and tamping of basic subject knowledge.",
    "country": "China",
    "code": "CN113516574A",
    "title": "Self-adaptive learning system based on big data and deep learning and construction method thereof",
    "link": "https://patents.google.com/patent/CN113516574A/en",
    "source": "google patent",
    "applicants": [
      "Beijing Aixuexi Bole Education Technology Co ltd"
    ]
  },
  {
    "_id": "66321b0884889bd0e1a87a88",
    "inventor_name": [
      "孟红",
      "唐振坤"
    ],
    "assignee_name_orig": [
      "Qiyuan World (beijing) Information Technology Service Co Ltd"
    ],
    "assignee_name_current": [
      "Qiyuan World (beijing) Information Technology Service Co Ltd"
    ],
    "pub_date": "2019-06-07",
    "priority_date": "",
    "grant_date": "2019-12-17",
    "filing_date": "",
    "forward_cite_no_family": [],
    "forward_cite_yes_family": [
      {
        "patent_number": "CN111830971B",
        "priority_date": "2020-06-15",
        "pub_date": "2021-09-07"
      },
      {
        "patent_number": "CN112114592B",
        "priority_date": "2020-09-10",
        "pub_date": "2021-12-17"
      },
      {
        "patent_number": "CN112381237B",
        "priority_date": "2020-12-09",
        "pub_date": "2022-04-22"
      },
      {
        "patent_number": "CN112396501A",
        "priority_date": "2020-12-10",
        "pub_date": "2021-02-23"
      }
    ],
    "backward_cite_no_family": [
      {
        "patent_number": "CN108393888A",
        "priority_date": "2017-02-06",
        "pub_date": "2018-08-14"
      },
      {
        "patent_number": "CN108406767A",
        "priority_date": "2018-02-13",
        "pub_date": "2018-08-17"
      }
    ],
    "backward_cite_yes_family": [
      {
        "patent_number": "US6917925B2",
        "priority_date": "2001-03-30",
        "pub_date": "2005-07-12"
      },
      {
        "patent_number": "US10452816B2",
        "priority_date": "2016-02-08",
        "pub_date": "2019-10-22"
      },
      {
        "patent_number": "CN107263449B",
        "priority_date": "2017-07-05",
        "pub_date": "2020-01-10"
      },
      {
        "patent_number": "CN108407921B",
        "priority_date": "2018-05-29",
        "pub_date": "2020-05-15"
      }
    ],
    "abstract_text": "The invention belongs to the technical field of artificial intelligence, and discloses an autonomous learning method and system for an intelligent agent facing man-machine cooperative work. The system comprises a cooperative agent, a simulation agent and a server. The invention can adapt to the dynamic change of the environment through the scheme, obtain the same performance effect in the similar environment, and can simulate the demonstration behaviors of different teachers, so that the trained intelligence can adapt to the dynamic change of the teachers, and can achieve the same cooperation effect for the teachers with different operation levels.",
    "country": "China",
    "code": "CN109858574B",
    "title": "Autonomous learning method and system for intelligent agent for man-machine cooperative work",
    "link": "https://patents.google.com/patent/CN109858574B/en",
    "source": "google patent",
    "applicants": [
      "Qiyuan World (beijing) Information Technology Service Co Ltd"
    ]
  }
]




app.secret_key = "secret_key"  

client = MongoClient("mongodb+srv://aymanemaghouti:FwbFRrymX6wjJPxG@patents.js05fnq.mongodb.net/?retryWrites=true&w=majority")
db = client.get_database("patent_db")


# Access the google_patents collection
patents_collection = db.google_patents

users_collection = db.users
user_records = db.user_records

def fetch_patents():
    mongodb_documents = []
    # for patent in patents_collection.find({}):
    #     mongodb_documents.append(patent)
    # return mongodb_documents
    return docs

# todo
def fetch_panier(user):
    all_patents = fetch_patents()

    selected_patents = []
    for patent in all_patents:
        for patent_id in user.get('patents', []):
            if str(patent['_id']) == str(patent_id):
                selected_patents.append(patent)
    return selected_patents


previous = 1
page = 2
nbrPages = 5
next = 3
rowNbr = 10

@app.route('/')
def home():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})

        selected_patents = fetch_panier(user)

        return render_template('home.html', username=session['email'], all_patents=docs, selected_patents=selected_patents, previous=previous, page=page, nbrPages=nbrPages, next=next, rowNbr=rowNbr)
    else:
            return render_template('login.html')
    

@app.route('/insight')
def insight():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})

        return render_template('insight.html', username=session['email'])
    else:
        return render_template('login.html')


@app.route('/search_patents')
def search_patents():
    user_email = session['email']
    user = users_collection.find_one({'email': user_email})
    query = request.args.get('query', '')
    search_results = search_title(query)
    selected_patents = fetch_panier(user)
    return render_template('home.html', all_patents=search_results,selected_patents=selected_patents)




@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})
        if user:
            record_id = request.json['record_id']
            users_collection.update_one(
                {'email': user_email},
                {'$addToSet': {'patents': record_id}}
            )
            return jsonify({'message': 'Record added to cart successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'User not logged in'}), 401


@app.route('/delete_patent', methods=['POST'])
def delete_patent():
    if 'email' in session:
        user_email = session['email']
        user = users_collection.find_one({'email': user_email})
        if user:
            record_id = request.json['record_id']
            print(ObjectId(record_id))
            users_collection.update_one(
                {'email': user_email},
                {'$pull': {'patents': str(record_id)}}
            )
            return jsonify({'message': 'Patent deleted successfully'}), 200
        else:
            return jsonify({'error': 'User not found'}), 404
    else:
        return jsonify({'error': 'User not logged in'}), 401




@app.route('/patent/<patent_id>')
def patent_details(patent_id):
    print(patent_id)
    patent = patents_collection.find_one({'_id': ObjectId(patent_id)})
    print(patent)

    if patent:

        if patent['source'] == 'google patenffft':

            patent['inventor_name'] = json.loads(patent['inventor_name'])
            patent['assignee_name_orig'] = json.loads(patent['assignee_name_orig'])
            patent['assignee_name_current'] = json.loads(patent['assignee_name_current'])

        return render_template('patent_details.html', patent=patent)
    else:
        # If patent is not found, render an error page or redirect to another route
        return render_template('patent_details.html', message='Patent not found')




@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email-I']
        password = request.form['password1-I']
        username = request.form['username-I']

        existing_user = users_collection.find_one({'email': email})
        if existing_user:
            return 'That email already exists!'

        hash_pass = generate_password_hash(password)
        users_collection.insert_one({'username':username ,'email': email, 'password': hash_pass})
        session['email'] = email
        session['username']=username
        return redirect('/')
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email-C']
        password = request.form['password-C']

        existing_user = users_collection.find_one({'email': email})
        if existing_user and check_password_hash(existing_user['password'], password):
            session['email'] = email
            return redirect('/')
        return 'Invalid email/password combination'
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('email', None)
    return redirect('/')

@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
