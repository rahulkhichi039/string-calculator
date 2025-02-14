import re

class StringCalculator:
    def add(self, numbers: str) -> int:
        if not numbers:
            return 0

        delimiter = ','
        if numbers.startswith('//'):
            parts = numbers.split('\n', 1)
            delimiter = self.extract_delimiters(parts[0][2:])
            numbers = parts[1]

        numbers = re.split(delimiter, numbers.replace('\n', ','))

        num_list = [int(num) for num in numbers if num]

        negatives = [num for num in num_list if num < 0]
        if negatives:
            raise ValueError(f"Negative numbers not allowed: {negatives}")

        return sum(num for num in num_list if num <= 1000)

    def extract_delimiters(self, delimiter_section: str) -> str:
        if delimiter_section.startswith('[') and delimiter_section.endswith(']'):
            delimiters = re.findall(r'\[(.*?)\]', delimiter_section)
            return '|'.join(map(re.escape, delimiters))
        return re.escape(delimiter_section)