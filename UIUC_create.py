from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import sys 

#cal_id = '32l623q7v98fmtf7h0os4660hk@group.calendar.google.com' 
cal_id = 'dr5qj5vv319gv64du4gr6ve4fg@group.calendar.google.com'

def usage():
   print("Correct data.txt file")

def main(year, month, day): #located in data.txt 
   service = get_calendar_service()


   d = datetime.now().date()
   
   # Physics # 

   # lab class  
   tomorrow = datetime(year, month, day, 12)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1) + timedelta(minutes=50)).isoformat()

   event_result = service.events().insert(calendarId=cal_id,
       body={
           "summary": 'Physics: Elec & Mag Lab',
           "description": 'Physics lab section\nUrbana-Champaign Campus | Campus Instructional Facility | Room 4031',
           "start": {"dateTime": start, "timeZone": 'America/Chicago'},
           "end": {"dateTime": end, "timeZone": 'America/Chicago'},
       }
   ).execute()

   # Lecture
   tomorrow = datetime(year, month, day, 14) + timedelta(days=1)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(minutes=50)).isoformat()

   event_result = service.events().insert(calendarId=cal_id,
       body={
           "summary": 'Physics: Elec & Mag Lecture',
           "description": 'Physics lecture section\nUrbana-Champaign Campus | Loomis Laboratory | Room 141',
           "start": {"dateTime": start, "timeZone": 'America/Chicago'},
           "end": {"dateTime": end, "timeZone": 'America/Chicago'},
       }
   ).execute()

   tomorrow = datetime(year, month, day, 14) + timedelta(days=3)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(minutes=50)).isoformat()

   event_result = service.events().insert(calendarId=cal_id,
       body={
           "summary": 'Physics: Elec & Mag Lecture',
           "description": 'Physics lecture section\nUrbana-Champaign Campus | Loomis Laboratory | Room 141',
           "start": {"dateTime": start, "timeZone": 'America/Chicago'},
           "end": {"dateTime": end, "timeZone": 'America/Chicago'},
       }
   ).execute()

   # Discussion 
   tomorrow = datetime(year, month, day, 8) + timedelta(days=2)
   start = tomorrow.isoformat()
   end = (tomorrow + timedelta(hours=1) + timedelta(minutes=50)).isoformat()

   event_result = service.events().insert(calendarId=cal_id,
       body={
           "summary": 'Physics: Elec & Mag Discussion',
           "description": 'Physics discussion section\nUrbana-Champaign Campus | Loomis Laboratory | Room 258',
           "start": {"dateTime": start, "timeZone": 'America/Chicago'},
           "end": {"dateTime": end, "timeZone": 'America/Chicago'},
       }
   ).execute()


   # Calculus III # 

   # Online Lecture 
   for delta in range(0, 5, 2):    
      tomorrow = datetime(year, month, day, 15) + timedelta(days=delta)
      start = tomorrow.isoformat()
      end = (tomorrow + timedelta(minutes=50)).isoformat()

      event_result = service.events().insert(calendarId=cal_id,
          body={
              "summary": 'Calculus III Lecture',
              "description": 'Calculus III online lecture section\nTBD',
              "start": {"dateTime": start, "timeZone": 'America/Chicago'},
              "end": {"dateTime": end, "timeZone": 'America/Chicago'},
          }
      ).execute()

   # Discussion 
   for delta in range(1, 4, 2): 
      tomorrow = datetime(year, month, day, 9) + timedelta(days=delta)
      start = tomorrow.isoformat()
      end = (tomorrow + timedelta(minutes=50)).isoformat()

      event_result = service.events().insert(calendarId=cal_id,
          body={
              "summary": 'Calculus III Discussion',
              "description": 'Calculus III discussion section\nUrbana-Champaign Campus | David Kinley Hall | Room 307',
              "start": {"dateTime": start, "timeZone": 'America/Chicago'},
              "end": {"dateTime": end, "timeZone": 'America/Chicago'},
          }
      ).execute()

   # Engineering Orientation #

   # Lecture
   for delta in range(1, 4, 2):
      tomorrow = datetime(year, month, day, 12) + timedelta(days=delta)
      start = tomorrow.isoformat()
      end = (tomorrow + timedelta(minutes=50)).isoformat()

      event_result = service.events().insert(calendarId=cal_id,
          body={
              "summary": 'Engineering Orientation Lecture',
              "description": 'Engineering orientation lecture section\nUrbana-Champaign Campus | Sidney Lu Mech Engr Bldg | Room 3100',
              "start": {"dateTime": start, "timeZone": 'America/Chicago'},
              "end": {"dateTime": end, "timeZone": 'America/Chicago'},
          }
      ).execute()

   # Computer Science Freshman Orientation #

   # Lecture
   for delta in range(4, 5, 2):
      tomorrow = datetime(year, month, day, 11) + timedelta(days=delta)
      start = tomorrow.isoformat()
      end = (tomorrow + timedelta(minutes=50)).isoformat()

      event_result = service.events().insert(calendarId=cal_id,
          body={
              "summary": 'CS Freshman Orientation Lecture',
              "description": 'CS freshman orientation lecture section\nUrbana-Champaign Campus | Foellinger Auditorium | Room AUD',
              "start": {"dateTime": start, "timeZone": 'America/Chicago'},
              "end": {"dateTime": end, "timeZone": 'America/Chicago'},
          }
      ).execute()

   # Viking Mythology # 

   # Lecture 
   for delta in range(4, 5, 2):
      tomorrow = datetime(year, month, day, 13) + timedelta(days=delta)
      start = tomorrow.isoformat()
      end = (tomorrow + timedelta(minutes=50)).isoformat()

      event_result = service.events().insert(calendarId=cal_id,
          body={
              "summary": 'Viking Mythology Lecture',
              "description": 'Viking mythology lecture section\nUrbana-Champaign Campus | Armory | Room 430',
              "start": {"dateTime": start, "timeZone": 'America/Chicago'},
              "end": {"dateTime": end, "timeZone": 'America/Chicago'},
          }
      ).execute()

   # Intro to Computer Science I # 
 
   # Lab 
   for delta in range(1, 2, 2):
      tomorrow = datetime(year, month, day, 16) + timedelta(days=delta)
      start = tomorrow.isoformat()
      end = (tomorrow + timedelta(minutes=50)).isoformat()

      event_result = service.events().insert(calendarId=cal_id,
          body={
              "summary": 'Intro to CS I Lab',
              "description": 'Intro to CS I lab section\nTBD',
              "start": {"dateTime": start, "timeZone": 'America/Chicago'},
              "end": {"dateTime": end, "timeZone": 'America/Chicago'},
          }
      ).execute()




if __name__ == '__main__':
   #Init from file (get the data) 
   f = open("data.txt", "r") 
   
   year = f.readline()
   month = f.readline()
   day = f.readline() 

   if(int(day) > 31):
      usage()
      sys.exit(1)
   main(int(year), int(month), int(day))
