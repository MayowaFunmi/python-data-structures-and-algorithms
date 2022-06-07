import tkinter.messagebox
from tkinter import *
from tkinter.ttk import Combobox

win = Tk()
win.geometry('1360x700')
win.title('Registration Form')
win['bg'] = 'red'

# creating data selection variable on gui
name = StringVar()
password = StringVar()
contact = StringVar()
email = StringVar()
age = StringVar()
gender = IntVar()
country = StringVar()
checkbox1 = IntVar()
checkbox2 = IntVar()
checkbox3 = IntVar()


#reset values
def clear():
    name.set('')
    password.set('')
    contact.set('')
    email.set('')
    age.set('0')
    country.set('0')
    gender.set('')
    checkbox1.set('0')
    checkbox2.set('0')
    checkbox3.set('0')


# callback function
def checkname(name):
    if name.isalnum():
        return True
    else:
        tkinter.messagebox.showwarning('Invalid Input', 'Empty Value Not llowed')



# form title
label_title = Label(win, text='Registration Form', width=20, font=('Calibri', 20, 'bold')).place(x=50, y=50)

# create fields
label_name = Label(win, text='Name', width=20).place(x=80, y=130)
entry_name = Entry(win, width=20, textvariable=name)
entry_name.place(x=300, y=130)
validate_name = win.register(checkname) # callback
entry_name.config(validate='key', validatecommand=(validate_name, '%P'))    #bind

label_password = Label(win, text='Password', width=20).place(x=80, y=180)
entry_password = Entry(win, width=20, textvariable=password, show='*').place(x=300, y=180)

label_contact = Label(win, text='Contact', width=20).place(x=80, y=230)
entry_contact = Entry(win, width=20, textvariable=contact).place(x=300, y=230)

label_email = Label(win, text='Email', width=20).place(x=80, y=280)
entry_email = Entry(win, width=20, textvariable=email).place(x=300, y=280)

label_age = Label(win, text='Age', width=20).place(x=80, y=330)
entry_age = Spinbox(win, textvariable=age, from_=1, to_=150).place(x=300, y=330)

label_gender = Label(win, text='Gender', width=20).place(x=80, y=380)
g_radio_male = Radiobutton(win, text='Male', padx=5, variable=gender, value=1).place(x=300, y=380)
g_radio_female = Radiobutton(win, text='Female', padx=5, variable=gender, value=2).place(x=300, y=430)

label_country = Label(win, text='Country', width=20).place(x=80, y=480)
list1 = ['Aruba', 'Afghanistan', 'Angola', 'Anguilla', 'Åland Islands', 'Albania', 'Andorra', 'United Arab Emirates',
         'Argentina', 'Armenia', 'American Samoa', 'Antarctica', 'French Southern Territories', 'Antigua and Barbuda',
         'Australia', 'Austria', 'Azerbaijan', 'Burundi', 'Belgium', 'Benin', 'Bonaire, Sint Eustatius and Saba',
         'Burkina Faso', 'Bangladesh', 'Bulgaria', 'Bahrain', 'Bahamas', 'Bosnia and Herzegovina', 'Saint Barthélemy',
         'Belarus', 'Belize', 'Bermuda', 'Bolivia, Plurinational State of', 'Brazil', 'Barbados', 'Brunei Darussalam',
         'Bhutan', 'Bouvet Island', 'Botswana', 'Central African Republic', 'Canada', 'Cocos (Keeling) Islands',
         'Switzerland', 'Chile', 'China', "Côte d'Ivoire", 'Cameroon', 'Congo, The Democratic Republic of the', 'Congo',
         'Cook Islands', 'Colombia', 'Comoros', 'Cabo Verde', 'Costa Rica', 'Cuba', 'Curaçao', 'Christmas Island',
         'Cayman Islands', 'Cyprus', 'Czechia', 'Germany', 'Djibouti', 'Dominica', 'Denmark', 'Dominican Republic',
         'Algeria', 'Ecuador', 'Egypt', 'Eritrea', 'Western Sahara', 'Spain', 'Estonia', 'Ethiopia', 'Finland', 'Fiji',
         'Falkland Islands (Malvinas)', 'France', 'Faroe Islands', 'Micronesia, Federated States of', 'Gabon',
         'United Kingdom', 'Georgia', 'Guernsey', 'Ghana', 'Gibraltar', 'Guinea', 'Guadeloupe', 'Gambia',
         'Guinea-Bissau', 'Equatorial Guinea', 'Greece', 'Grenada', 'Greenland', 'Guatemala', 'French Guiana',
         'Guam', 'Guyana', 'Hong Kong', 'Heard Island and McDonald Islands', 'Honduras', 'Croatia', 'Haiti',
         'Hungary', 'Indonesia', 'Isle of Man', 'India', 'British Indian Ocean Territory', 'Ireland',
         'Iran, Islamic Republic of', 'Iraq', 'Iceland', 'Israel', 'Italy', 'Jamaica', 'Jersey', 'Jordan', 'Japan',
         'Kazakhstan', 'Kenya', 'Kyrgyzstan', 'Cambodia', 'Kiribati', 'Saint Kitts and Nevis', 'Korea, Republic of',
         'Kuwait', "Lao People's Democratic Republic", 'Lebanon', 'Liberia', 'Libya', 'Saint Lucia', 'Liechtenstein',
         'Sri Lanka', 'Lesotho', 'Lithuania', 'Luxembourg', 'Latvia', 'Macao', 'Saint Martin (French part)', 'Morocco',
         'Monaco', 'Moldova, Republic of', 'Madagascar', 'Maldives', 'Mexico', 'Marshall Islands', 'North Macedonia',
         'Mali', 'Malta', 'Myanmar', 'Montenegro', 'Mongolia', 'Northern Mariana Islands', 'Mozambique', 'Mauritania',
         'Montserrat', 'Martinique', 'Mauritius', 'Malawi', 'Malaysia', 'Mayotte', 'Namibia', 'New Caledonia', 'Niger',
         'Norfolk Island', 'Nigeria', 'Nicaragua', 'Niue', 'Netherlands', 'Norway', 'Nepal', 'Nauru', 'New Zealand',
         'Oman', 'Pakistan', 'Panama', 'Pitcairn', 'Peru', 'Philippines', 'Palau', 'Papua New Guinea', 'Poland',
         'Puerto Rico', "Korea, Democratic People's Republic of", 'Portugal', 'Paraguay', 'Palestine, State of',
         'French Polynesia', 'Qatar', 'Réunion', 'Romania', 'Russian Federation', 'Rwanda', 'Saudi Arabia', 'Sudan',
         'Senegal', 'Singapore', 'South Georgia and the South Sandwich Islands',
         'Saint Helena, Ascension and Tristan da Cunha', 'Svalbard and Jan Mayen', 'Solomon Islands', 'Sierra Leone',
         'El Salvador', 'San Marino', 'Somalia', 'Saint Pierre and Miquelon', 'Serbia', 'South Sudan',
         'Sao Tome and Principe', 'Suriname', 'Slovakia', 'Slovenia', 'Sweden', 'Eswatini', 'Sint Maarten (Dutch part)',
         'Seychelles', 'Syrian Arab Republic', 'Turks and Caicos Islands', 'Chad', 'Togo', 'Thailand', 'Tajikistan',
         'Tokelau', 'Turkmenistan', 'Timor-Leste', 'Tonga', 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Tuvalu',
         'Taiwan, Province of China', 'Tanzania, United Republic of', 'Uganda', 'Ukraine',
         'United States Minor Outlying Islands', 'Uruguay', 'United States', 'Uzbekistan', 'Holy See (Vatican City State)',
         'Saint Vincent and the Grenadines', 'Venezuela, Bolivarian Republic of', 'Virgin Islands, British',
         'Virgin Islands, U.S.', 'Viet Nam', 'Vanuatu', 'Wallis and Futuna', 'Samoa', 'Yemen', 'South Africa', 'Zambia',
         'Zimbabwe']

droplist = Combobox(win, width=15, textvariable=country)
droplist['values'] = list1
droplist.place(x=300, y=480)
droplist.current(0)
'''
droplist = OptionMenu(win, country, *list1)
droplist.config(width=15)
country.set('Select Your Country')
droplist.place(x=300, y=480)
'''


label_prog = Label(win, text='Programming', width=20).place(x=80, y=530)
entry_check1 = Checkbutton(win, text='Python', variable=checkbox1).place(x=300, y=530)
entry_check2 = Checkbutton(win, text='Javascript', variable=checkbox2).place(x=360, y=530)
entry_check3 = Checkbutton(win, text='Django', variable=checkbox3).place(x=420, y=530)

Button(win, text='Submit', width=10, bg='blue', fg='white').place(x=80, y=570)
Button(win, text='Clear Data', width=10, bg='blue', fg='white', command=clear).place(x=230, y=570)
Button(win, text='Check', width=10, bg='blue', fg='white').place(x=380, y=570)


win.mainloop()