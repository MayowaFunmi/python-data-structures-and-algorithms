import pathlib
import csv

# define varianles
subject_list = []
start_hour = 8
next_hour = 9
school_days = ['monday', 'tuesday']
time_slot_list = [] # list of time slot
subject_per_slot = {}
MAX_HOUR_PER_SUBJECT = 6
subject_hour_count = {}

# fill in subjects
# method 1

# def fill_in_subjects_list():
#     """
#     Ask users subjects and fill in subjects list
#     """
#     enter_another_subject = True
#     while enter_another_subject:
#         subject = input('Type another subject: ')
#         subject = subject.capitalize()

#         if not subject in subject_list:
#             subject_list.append(subject)
#             subject_hour_count[subject] = MAX_HOUR_PER_SUBJECT
#         else:
#             print(f'You have already added {subject} in your list')
        
#         question = input('Do you want to enter another subject? (y for yes and n for no: )')
#         if question.lower() == 'n':
#             enter_another_subject = False
#         elif question.lower() == 'y':
#             enter_another_subject = True

# method 2

def fill_out_subjects_list():
    """
    Ask users subjects and fill in subjects list
    """
    subjects = input('Type all subjects you want to add in your subject list and separate them by comma: ')
    the_subjects = subjects.replace(', ', ',') # remove space after comma
    the_subjects = the_subjects.split(',')

    for subject in the_subjects:
        subject = subject.capitalize()
        if not subject in subject_list:
            subject_list.append(subject)
            subject_hour_count[subject] = MAX_HOUR_PER_SUBJECT

def ask_hour():
    """Ask hour to user"""
    print(f'Subjects list: {subject_list}')
    print(f'Planning time: {start_hour}h - {next_hour}h')
    user_answer = input('What subject do you want to put here? ')
    return user_answer

def fill_in_timetable():
    """Display an hour and ask user which subject he wants to put there"""
    global start_hour
    global next_hour

    for day in school_days:
        # reset start and next hours
        the_hour = {}
        time = 0
        start_hour = 8
        next_hour = 9

        print('\n=====================================')
        print(f'{day.capitalize()} timetable')
        print('\n=====================================')

        while time < 6:
            hour_format = f'{start_hour}h - {next_hour}h'
            if time == 4:   # take a break
                subject_per_slot[hour_format] = ['Break time']

                if not hour_format in time_slot_list:
                    time_slot_list.append(hour_format)
            else:
                chosen_subject = ask_hour().capitalize()
                print(f'start_hour: {start_hour}')
                print(f'next_hour: {next_hour}')

                # check that subject chosen by user is in suject list
                while not chosen_subject in subject_list:
                    print(f'{chosen_subject} is not in your list of subjects')
                    print('Please choose another subject: ')
                    chosen_subject = ask_hour().capitalize()

                # add hour format while making sure we avoid duplicate
                if not hour_format in time_slot_list:
                    time_slot_list.append(hour_format)
                    subject_per_slot[hour_format] = [chosen_subject]
                else:
                    subject_per_slot[hour_format] += [chosen_subject]

                # check that chosen subject max hours is not reached
                for subject, max_hour in subject_hour_count.items():
                    if chosen_subject == subject:
                        # remove one hour from subject max hour
                        subject_hour_count[chosen_subject] = max_hour - 1

            # go to next hour
            start_hour += 1
            next_hour += 1
            time += 1

# scenario
fill_out_subjects_list()
fill_in_timetable()
print(f'Subject per slot: {subject_per_slot}')

timetable_path = pathlib.Path.cwd() / 'timetable.csv'

# save time tavble into a csv file

with open(timetable_path, 'w') as timetable_file:
    timetable_writing = csv.writer(timetable_file)

    # write headers into csv file
    csv_headers = ['Hours']
    csv_headers.extend(school_days)
    timetable_writing.writerow(csv_headers)

    # write content into csv file
    for time_slot, concerned_subjects in subject_per_slot.items():
        time_line = [time_slot]
        concerned_subjects_list = []

        if concerned_subjects == ['Break time']:
            for x in range(0, len(school_days)):
                concerned_subjects_list.append('Break time')
        else:
            concerned_subjects_list = concerned_subjects

        final_line = time_line + concerned_subjects_list
        timetable_writing.writerow(final_line)
    print('Your timetable is ready')
    