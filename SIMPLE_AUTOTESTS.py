from functions import salary,hello_who

assert hello_who('Max') == 'Hello,Max', 'Hello who error'
assert hello_who('Leo') == 'Hello,Leo', 'Hello who error'
assert hello_who('Nikita') == 'Hello,Nikita', 'Hello who error'
assert salary(hours: 2, salary_by_hours: 1) == 4
assert salary(hours: 2, salary_by_hours: 2) == 8