from datetime import datetime
from mailmerge import MailMerge

def generate_word_resume(data, translations, output_path, tldr:bool = False):
    """
    Generate a Word resume from a template and save it to the specified output path.

    Args:
        data (dict): The resume data to be included in the template.
        translations (dict): The translations for different text elements in the template.
        output_path (str): The path where the generated Word file will be saved.

    Returns:
        None
    """
    if tldr:
        template_path = 'templates/resume_tldr_template.docx'  # Path to your Word template
    else:
        template_path = 'templates/resume_template.docx'  # Path to your Word template

    with MailMerge(template_path) as document:
        # Mapping the new JSON structure to the template fields
        merge_data = {
            'name': data['name'],
            'phone': data['contact']['phone'],
            'email': data['contact']['email'],
            'location': data['contact']['location'],
            'summary': data['contact']['summary'],
            'year': datetime.now().year
        }

        # Adding social media links
        social_media = ', '.join(data['contact']['social_media'])
        merge_data['social_media'] = social_media

        # Add translations for headers
        merge_data.update({
            'trl_profile': translations['profile'],
            'trl_contact': translations['contact'],
            'trl_education': translations['education'],
            'trl_skills': translations['skills'],
            'trl_experience': translations['work_experience'],
            'trl_projects': translations['hobby_projects']
        })

        # Add education details
        for i, edu in enumerate(data['education'], start=1):
            merge_data.update({
                f'edu_degree_{i}': edu['degree'],
                f'edu_institution_{i}': edu['institution'],
                f'edu_major_{i}': edu.get('major', ''),
                f'edu_dates_{i}': edu['dates'],
                f'edu_cgpa_{i}': edu.get('cgpa', edu.get('percentage', ''))
            })

        # Add skills
        merge_data['skills_programming_languages'] = ', '.join(data['skills']['programming_languages'])
        merge_data['skills_frameworks'] = ', '.join(data['skills']['frameworks'])
        merge_data['skills_tools'] = ', '.join(data['skills']['tools'])

        # Add work experience details
        for i, job in enumerate(data['experience'], start=1):
            merge_data.update({
                f'work_title_{i}': job['title'],
                f'work_company_{i}': job['company'],
                f'work_location_{i}': job['location'],
                f'work_dates_{i}': job['dates'],
                f'work_responsibilities_{i}': '\n'.join(job['responsibilities'])
            })

        # Add projects details
        for i, proj in enumerate(data['projects'], start=1):
            merge_data.update({
                f'project_name_{i}': proj['name'],
                f'project_technologies_{i}': ', '.join(proj['technologies']),
                f'project_date_{i}': proj['date'],
                f'project_description_{i}': proj['description']
            })

        document.merge(**merge_data)
        document.write(output_path)
