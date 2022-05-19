class Service:

    def read_text(self, prompt):
        return input(prompt)

    def read_number(self, prompt):
        return float(input(prompt))

    def write_text(self, text):
        print(text)