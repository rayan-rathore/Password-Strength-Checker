
class Scorer:
    def __init__(self):
        self.password_score = 0
        self.feedback_list = []

    def calculate_score(self, data):
        self.password_score = 0
        self.feedback_list = []

        if data["Is_Common"]:
            self.password_score = 0
            self.feedback_list.append("CRITICAL: This password is among the most commonly "
                                      "used passwords and is easily hacked!")
            return self.password_score, self.feedback_list

        if data["Chunk_Repeat"]:
            self.password_score -= 1
            self.feedback_list.append("Repeating pattern detected (e.g., 'abcabc').")
        if data["Char_Repeat"]:
            self.password_score -= 3
            self.feedback_list.append("Character spam detected (e.g., 'aaa').")

        if data["Has_Sequences"]:
            self.password_score -= 2
            self.feedback_list.append("Avoid using keyboard paths or "
                                      "sequential letters/numbers (like 'qwerty' or '1234').")

        if data["Length"] >= 14:
            self.password_score += 2
        elif data["Length"] >= 8:
            self.password_score += 1
        else:
            self.feedback_list.append("Warning: Password is too short (minimum 8 characters required.).")


        if data["Uppercase"]["status"]:
            self.password_score += 2
        else:
            self.feedback_list.append("Add an uppercase letter (e.g., A, B, C).")

        if data["Lowercase"]["status"]:
            self.password_score += 2
        else:
            self.feedback_list.append("Add a Lowercase letter (e.g., a, b, c).")

        if data["Numbers"]["status"]:
            self.password_score += 2
        else:
            self.feedback_list.append("Add Some Numbers (e.g., 0, 1, 2).")

        if data["Symbols"]["status"]:
            self.password_score += 2
        else:
            self.feedback_list.append("Add a special character (e.g., !, @, #)")

        return self.password_score, self.feedback_list
