with open('files/write.txt', 'w') as write_file:
    write_file.write('Oh! Kolawole, Python and JavaScript are interesting!!')

with open('files/write.txt', 'a') as write_file:
    write_file.write('\nI Love Python so much')


quotes = [

    "\nThere is nothing more attractive than confidence, once you see your own beauty, so will everyone else",
    "\nSuccess comes to those who are hones and confident in their endeavour",
    "\nEducation is ability to listen to almost anything withous loosing your temper on your self-confidence",
    "\nYou can cry all you want but it wont help. You have to take action . Take control, make someone see, make someone hear you"

]

with open('files/write.txt', 'a') as write_file:
    write_file.writelines(quotes)
