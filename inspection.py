import re
from data import KEYBOARD_ROWS



class Inspection:
    def __init__(self, password):
        self.password = password
        self.length = 0
        self.has_upper = False
        self.has_lower = False
        self.has_digit = False
        self.has_special = False

    def evaluation(self):
        leet_mapping = {
            "@": "a",
            "0": "o",
            "3": "e",
            "$": "s",
        }

        with open("10k-most-common.txt", mode="r", encoding="utf-8") as file:
            com_pass = [line.strip() for line in file if line.strip()]
        creative_password = self.password.lower()
        normalize_password = "".join(leet_mapping.get(char, char) for char in creative_password)

        if self.password.lower() in com_pass or normalize_password in com_pass:
            common_status =  True
        else:
            common_status = False
        return common_status

    def check_sequences(self):
        clean_password = self.password.lower()
        if len(self.password) >= 4:
            for i in range(len(clean_password) -3):
                slice_window = clean_password[i:i+4]
                for key , pattern in KEYBOARD_ROWS.items():
                    if slice_window in pattern or slice_window in pattern[::-1]:
                        return True
        return False

    def repeated_pattern(self):
        pattern = r"(.{2,})\1"  #Catch repeating multi-character sequences
        pattern1 = r"(.)\1{2}" #Catch 3 identical characters in a row
        repeating_pattern = bool(re.search(pattern,self.password, flags=re.IGNORECASE))
        excessive_repeats = bool(re.search(pattern1, self.password, flags=re.IGNORECASE))
        return repeating_pattern, excessive_repeats


    def analyze(self):
        common_result = self.evaluation()
        repeating_pattern, excessive_repeats = self.repeated_pattern()
        sequence = self.check_sequences()
        self.length = len(self.password)

        self.has_upper = bool(re.search(r'[A-Z]', self.password))
        u_count = len(re.findall(r'[A-Z]', self.password))

        self.has_lower = bool(re.search(r'[a-z]', self.password))
        l_count = len(re.findall(r'[a-z]', self.password))

        self.has_digit = bool(re.search(r'[0-9]', self.password))
        d_count = len(re.findall(r'[0-9]', self.password))

        self.has_special = bool(re.search(r'[^a-zA-Z0-9\s]', self.password))
        s_count = len(re.findall(r'[^a-zA-Z0-9\s]', self.password))

        evaluation_data = {"Is_Common" : common_result,
                "Chunk_Repeat": repeating_pattern, "Char_Repeat" : excessive_repeats,
                "Has_Sequences": sequence,
                "Length": self.length,
                "Uppercase": {"status": self.has_upper, "count": u_count},
                "Lowercase": {"status": self.has_lower, "count": l_count},
                "Numbers": {"status": self.has_digit, "count": d_count},
                "Symbols" : {"status": self.has_special,"count": s_count}
                }

        return evaluation_data

