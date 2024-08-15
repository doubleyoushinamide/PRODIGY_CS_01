from pyfiglet import Figlet

def print_title(title, additional_text):
    # Create a Figlet font object with 'big' font
    figlet = Figlet(font='big')

    # Generate ASCII art for the title
    ascii_art = figlet.renderText(title)

    # Combining the additional text with the ASCII art
    # The additional text should be centered relative to the ASCII art
    # Finding the width of the ASCII art
    ascii_art_lines = ascii_art.split('\n')
    width = max(len(line) for line in ascii_art_lines)

    # Justify-left the additional text
    extra_additional_text = additional_text.rjust(width)

    # Combine the text and ASCII art
    combined_output = f"{extra_additional_text}\n{ascii_art}"

    # Print the combined output
    print(combined_output)
