class Book:

    def __init__(
        self, author, main_character, time_period, target_audience, ending
    ):
        self.author = author
        self.main_character = main_character
        self.time_period = time_period
        self.target_audience = target_audience
        self.ending = ending
        self.fanworks = []  # Added initialization for fanworks list

    def read_summary(self):
        print(f"\n--- Reading Book Summary ---")
        author = input("Who is the author of the book?: ")
        main_character = input("Who is the main character of the book?: ")
        time_period = int(input("What is the time period of the book?: "))
        target_audience = input("Who is the target audience of the book?: ")
        ending = input("What is the ending of the book?: ")

    def research_lore(self):
        topic_ = input(
            "Type the missing lore or unresolved mystery you want to research: "
        )
        print(
            f"Searching archives for '{topic_}' featuring {self.main_character}..."
        )
        return topic_

    def create_fanwork(self, topic_):
        work_title = input("Enter your fanwork's title: ")
        full_title = (
            f"'{work_title}' ({self.author} Lore: {topic_} - {self.time_period})"
        )
        self.fanworks.append(full_title)  # Appends created fanwork to the list
        print(f"Fanwork '{full_title}' created!")

    def delete_fanwork(self):
        if not self.fanworks:
            print("No fanworks available to delete.")
            return

        print("\nYour Fanworks:")
        for idx, work in enumerate(self.fanworks, 1):
            print(f"{idx}. {work}")

        name_to_delete = input(
            "\nEnter the name or number of the fanwork to delete: "
        )

        # Check if user entered a number index
        if name_to_delete.isdigit():
            index = int(name_to_delete) - 1
            if 0 <= index < len(self.fanworks):
                removed = self.fanworks.pop(index)
                print(f"Deleted fanwork: '{removed}'")
                return

        # Check if user entered the exact title/string
        for work in self.fanworks:
            if name_to_delete.lower() in work.lower():
                self.fanworks.remove(work)
                print(f"Deleted fanwork: '{work}'")
                return

        print("Fanwork not found.")       



                                    
                                
                    
  
