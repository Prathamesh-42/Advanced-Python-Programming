# Decorator for bold formatting
def bold_text(func):
    def wrapper(self):
        return "**" + func(self) + "**"
    return wrapper


# Report class
class Report:
    # Class variable to store templates
    templates = {}

    # Constructor
    def __init__(self, title, content):
        self.title = title
        self.content = content

    # Class method to add a template
    @classmethod
    def add_template(cls, name, func):
        cls.templates[name] = func

    # Class method to get a template
    @classmethod
    def get_template(cls, name):
        return cls.templates.get(name)

    # Magic method to call report with template name
    def __call__(self, template_name):
        template = self.get_template(template_name)
        if template:
            return template(self)
        else:
            return "Template not found."

    # String representation
    def __str__(self):
        return f"Title: {self.title}\nContent: {self.content}"


# Simple template
def simple_template(report):
    return f"Title: {report.title}\nContent: {report.content}"


# Fancy template with bold formatting
@bold_text
def fancy_template(report):
    return f"Title: {report.title}\nContent: {report.content}"


# Main function
def main():
    # Add templates
    Report.add_template("simple", simple_template)
    Report.add_template("fancy", fancy_template)

    # Create report object
    report = Report("Monthly Report", "Sales increased by 20%.")

    # Generate reports
    print("Simple Report:")
    print(report("simple"))

    print("\nFancy Report:")
    print(report("fancy"))


# Run the program
if __name__ == "__main__":
    main()