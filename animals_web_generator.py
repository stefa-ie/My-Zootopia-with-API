import data_fetcher
import os

def animal_card(animal_obj):
    """Generates an HTML card for a single animal object."""
    output = ""
    output += '<li class="cards__item">\n'
    
    # Always show name if available, otherwise show a default
    name = animal_obj.get('name', 'Unknown Animal')
    output += f"<div class='card__title'>{name}</div><br/>\n"
    
    output += "<p class='card__text'>\n"
    
    # Check for characteristics
    characteristics = animal_obj.get('characteristics', {})
    if isinstance(characteristics, dict):
        if 'diet' in characteristics:
            output += f"<strong>Diet:</strong> {characteristics['diet']}<br/>\n"
        if 'type' in characteristics:
            output += f"<strong>Type:</strong> {characteristics['type']}<br/>\n"
    
    # Check for locations
    locations = animal_obj.get('locations', [])
    if locations and isinstance(locations, list) and len(locations) > 0:
        output += f"<strong>Location:</strong> {locations[0]}<br/>\n"
    
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
        # If it's a single dict, wrap it in a list
        animals = [animal_data]
    else:
        # Fallback: try to iterate if it's iterable
        animals = list(animal_data) if hasattr(animal_data, '__iter__') else []
    
    if not animals:
        print(f"Warning: No animal data to display for '{animal_name}'.")
        return
    
    for animal in animals:
        if isinstance(animal, dict):
            output += animal_card(animal)
    
    # Ensure we have content to display
    if not output.strip():
        print(f"Warning: No valid animal data could be processed for '{animal_name}'.")
        return

    # Get the directory where this script is located
    script_dir = os.path.dirname(os.path.abspath(__file__))
    template_path = os.path.join(script_dir, 'animals_template.html')
    
    with open(template_path, 'r') as file:
        content = file.read()

    updated_content = content.replace('__REPLACE_ANIMALS_INFO__', output)

    output_path = os.path.join(script_dir, f'{animal_name}.html')
    with open(output_path, 'w') as file:
        file.write(updated_content)

    print(f"Created/Updated {animal_name}.html with information about {animal_name}.")


def main():
    animal_name = input("Please enter an animal: ")
    update_html(animal_name)


if __name__ == "__main__":
    main()

