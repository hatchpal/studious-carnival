
#--------------------------------------

# print('This is working')

# def main():

# 	top = ("template/top.html")
# 	bottom = ("template/bottom.html")
# 	about = ("content/about.html")
# 	experience = ("content/experience.html")
# 	skills = ("content/skills.html")
# 	contact = ("content/contact.html")

# #Combine top.html and bottom.html into base.html with {{content}}
# 	top_template = open(top).read()
# 	bottom_template = open(bottom).read()
# 	base_template = top_template + "{{content}}" + bottom_template
# 	open('template/base.html', 'w+').write(base_template)

# if __name__ == "__main__":
# 	main()


template = open("template/base.html").read()

# def combine_template():

# 	about = ("content/about.html")
# 	experience = ("content/experience.html")
# 	skills = ("content/skills.html")
# 	contact = ("content/contact.html")

# 	#Create an index.html page in docs folder
# 	index_content = open(about).read()
# 	finished_index_page = template.replace("{{content}}", index_content)
# 	open('docs/index.html', 'w+').write(finished_index_page)

# 	#Create an experience.html page in docs folder
# 	experience_content = open(experience).read()
# 	finished_experience_page = template.replace("{{content}}", experience_content)
# 	open('docs/experience.html', 'w+').write(finished_experience_page)

# 	#Create an skills.html page in docs folder
# 	skills_content = open(skills).read()
# 	finished_skills_page = template.replace("{{content}}", skills_content)
# 	open('docs/skills.html', 'w+').write(finished_skills_page)

# 	#Create an contact.html page in docs folder
# 	contact_content = open(contact).read()
# 	finished_contact_page = template.replace("{{content}}", contact_content)
# 	open('docs/contact.html', 'w+').write(finished_contact_page)

# 	return

# combine_template()

def listdic():

	pages = [
		{
			"filename": "content/about.html",
			"output": "docs/index.html",
			"title": "ABOUT",
		},
		{
			"filename": "content/experience.html",
			"output": "docs/experience.html",
			"title": "EXPERIENCE",
		},
		{
			"filename": "content/skills.html",
			"output": "docs/skills.html",
			"title": "SKILLS",
		},
		{
			"filename": "content/contact.html",
			"output": "docs/contact.html",
			"title": "CONTACT",
		}	
		]
	# template = open("template/base.html").read()

	for page in pages:
		filename = open(page['filename']).read()
		combined_file = template.replace("{{content}}", filename)
		combined_file = combined_file.replace("{{title}}", page['title']) 
		open(page['output'], 'w+').write(combined_file)


listdic()





# # # Breaking down into 2 other functions

# def apply_template():
# 	main()
# 	listdic()
# 	return
# apply_template()

