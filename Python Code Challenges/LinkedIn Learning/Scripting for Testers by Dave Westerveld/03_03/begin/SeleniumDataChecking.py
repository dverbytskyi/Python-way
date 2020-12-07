from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.hackerrank.com/dashboard')

skill_tags = driver.find_elements_by_class_name('track-name')

available_skills = []
for skill in skill_tags:
    available_skills.append(skill.text)

for skill in available_skills:
    print(skill)

driver.close()