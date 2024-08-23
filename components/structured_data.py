import json

def generate_structured_data(data, output_path):
    """
    Generate structured data in JSON-LD format and save it to the specified output path.

    Args:
        data (dict): The resume data from which structured data will be generated.
        output_path (str): The path where the generated JSON-LD file will be saved.

    Returns:
        None
    """
    # Create the structured data dictionary
    structured_data = {
        "@context": "https://schema.org",
        "@type": "Person",
        "name": data['name'],
        "jobTitle": "Software Engineer",  # Assuming 'Software Engineer' based on context
        "email": data['contact']['email'],
        "telephone": data['contact']['phone'],
        "address": {
            "@type": "PostalAddress",
            "addressLocality": data['contact']['location'],
            "addressCountry": "India"  # Assuming 'India' based on context
        },
        "sameAs": [f"https://{platform.lower()}.com/{data['name'].replace(' ', '').lower()}" for platform in data['contact']['social_media']],
        "worksFor": [
            {
                "@type": "Organization",
                "name": job['company'],
                "sameAs": "https://example.com"  # Placeholder URL
            } for job in data['experience']
        ]
    }

    # Write the structured data to the output path in JSON format
    with open(output_path, 'w') as file:
        json.dump(structured_data, file, indent=4)
