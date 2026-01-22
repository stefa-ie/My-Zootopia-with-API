import data_fetcher
import os

def animal_card(animal_obj):
    """Generates an HTML card for a single animal object."""
    output = ""
    output += '<li class="cards__item">\n'
    if 'name' in animal_obj:
        output += f"<div class='card__title'>{animal_obj['name']}</div><br/>\n"
    output += "<p class='card__text'>\n"
    if 'characteristics' in animal_obj and 'diet' in animal_obj['characteristics']:
        output += f"<strong>Diet:</strong> {animal_obj['characteristics']['diet']}<br/>\n"
    if 'locations' in animal_obj and animal_obj['locations']:
        output += f"<strong>Location:</strong> {animal_obj['locations'][0]}<br/>\n"
    if 'characteristics' in animal_obj and 'type' in animal_obj['characteristics']:
        output += f"<strong>Type:</strong> {animal_obj['characteristics']['type']}<br/>\n"
    output += '</p>\n'
    output += '</li>\n'
    return output


def update_html(animal_name):
    """Fetches animal data from API and updates/creates HTML file."""
    animal_data = data_fetcher.fetch_data(animal_name)

    if not animal_data:
        print(f"No data found for '{animal_name}'.")
        return

    output = ''
    # Handle different response formats
    if isinstance(animal_data, list):
        animals = animal_data
    elif isinstance(animal_data, dict):
        animals = [animal_data]
    else:
        animals = []
    
    # Check if we have any animals to display
    if not animals:
        print(f"No animal data to display for '{animal_name}'.")
        return
    
    for animal in animals:
        if isinstance(animal, dict):
            output += animal_card(animal)
    
    # Ensure we generated some content
    if not output.strip():
        print(f"Warning: Generated HTML is empty for '{animal_name}'. Check API response structure.")
        return

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'animals_template.html')
    
    with open(template_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Replace the marker - handle with or without surrounding whitespace
    if '__REPLACE_ANIMALS_INFO__' not in content:
        print(f"Error: Replacement marker '__REPLACE_ANIMALS_INFO__' not found in template!")
        return
    
    updated_content = content.replace('__REPLACE_ANIMALS_INFO__', output)
    
    # Debug: Check if replacement worked
    if '__REPLACE_ANIMALS_INFO__' in updated_content:
        print(f"Warning: Replacement marker not found or replacement failed!")
        print(f"Generated output length: {len(output)} characters")
    else:
        print(f"Successfully replaced content. Generated {len(animals)} animal card(s).")

    output_path = os.path.join(script_dir, f'{animal_name}.html')
    with open(output_path, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Created/Updated {animal_name}.html at: {output_path}")
    print(f"File size: {os.path.getsize(output_path)} bytes")


def main():
    animal_name = input("Please enter an animal: ")
    update_html(animal_name)


if __name__ == "__main__":
    main()

