#make Calender
import calendar
import datetime
import sys
import os
import time
#make a list of days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
#make a list of months
months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
#make a list of years
years = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
#make a list of times
times = ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"]
#make a list of days in a month
days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#Make calender
def calender():
    #make a list of days
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    #make a list of months
    months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    #make a list of years
    years = ["2021", "2022", "2023", "2024", "2025", "2026", "2027", "2028", "2029", "2030"]
    #make a list of times
    times = ["12:00 AM", "1:00 AM", "2:00 AM", "3:00 AM", "4:00 AM", "5:00 AM", "6:00 AM", "7:00 AM", "8:00 AM", "9:00 AM", "10:00 AM", "11:00 AM", "12:00 PM", "1:00 PM", "2:00 PM", "3:00 PM", "4:00 PM", "5:00 PM", "6:00 PM", "7:00 PM", "8:00 PM", "9:00 PM", "10:00 PM", "11:00 PM"]
    #make a list of days in a month
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    #give input
    month = input("Enter a month: ")
    day = input("Enter a day: ")
    year = input("Enter a year: ")
    #make a list of days in a month
    
#define int main
def main():
    #run calender function
    s = calender()
    #run time function
    time()