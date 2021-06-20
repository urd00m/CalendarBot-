from datetime import datetime, timedelta
from cal_setup import get_calendar_service
import sys 

from openpyxl import *
from tkinter import *

#TODO: Designed by Alan Wang


#cal_id = '32l623q7v98fmtf7h0os4660hk@group.calendar.google.com' 
cal_id = 'dr5qj5vv319gv64du4gr6ve4fg@group.calendar.google.com'

def prompt():
   print("\nUser menu:")
   print("1. Type help to view detailed feature information") #TODO
   print("2. Type add to add events to your saved calendar file (inputs.txt)") #TODO
   print("3. Type delete to delete events from your saved calendar file (inputs.txt)") #TODO
   print("4. Type ignore to temporarily ignore events from your saved calendar file (inputs.txt)") #TODO
   print("5. Type update to update your Google Calendar with your saved calendar file (inputs.txt)") #TODO
   print("6. Type list to view your saved calendar file events (inputs.txt)") #TODO
   print("7. Type undo to remove the recently added calendar events") #TODO
   print("8. Type quit to quit out of Calendar Bot") #TODO 
   ret = input("Please enter your selection: ")
   return ret 

# Year - int, month - int, day - int, hour - int, length(hours and minutes) - int, daysOfWeek - int[], title - string, description - string  
def event(year, month, day, hour, lengthHours, lengthMinutes, daysOfWeek, title, description): 
   for cur in daysOfWeek:
      tomorrow = datetime(year, month, day, hour) + timedelta(days=cur)
      start = tomorrow.isoformat()
      end = (tomorrow + timedelta(hours=lengthHours) + timedelta(minutes=lengthMinutes)).isoformat()
      event_result = service.events().insert(calendarId=cal_id,
          body={
              "summary": title,
              "description": description,
              "start": {"dateTime": start, "timeZone": 'America/Chicago'}, # All times are in chicago time (CST) 
              "end": {"dateTime": end, "timeZone": 'America/Chicago'},
          }
      ).execute()

def add():
   f = open("input.txt", "a") 
   print("To cancel this operation at any point type C (must be uppercase)\nAt any point if you wish to go back a step type UNDO (Must be uppercase)") 
   



def map(input):
   if(input.lower() == 'add' or input == '2'): # Adds something to input.txt
      add()
   # TODO 
   else:
      print("TODO")
      



if __name__ == '__main__':
   try: 
      f = open("input.txt", "r") 
   except OSError as e: 
      if(e.errno == 2):
         print("New input file needed, creating...") 
         f = open("input.txt", "w") # overwrite
         f.close()
         f = open("input.txt", "r") 
         print("New input file (input.txt) created, all user data will be stored in that file")
      else: 
         print("Unknown error occured, please attempt rerunning, or delete existing input.txt file or contact for further help")
         print("Program terminating")
         sys.exit(1)
   f.close() # Prevent clashes with later file opens 

   #TODO: Add in Ascii stuff to make it look cooler 
   # Start Up
   print("Hi I am Calendar Bot, a bot that can easily help you add events to your google calendar!") 
   print("All your data is stored, so when you add a calendar event I remember it so that you don't need to type it in again!")
   print("There are all sorts of features being offered with this bot, if you want to discover them all type help")

   input = prompt()
   while(input.lower() != 'quit' and input.lower() != 'q' and input.lower() != 'exit' and input != '8'): # User types in quit
      map(input) 
      input = prompt()
