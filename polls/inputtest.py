from models import Question

# Tạo một đối tượng Product mới
question = Question()

# Gán giá trị cho các trường của đối tượng
question.question_text = "2 + 2 = ?"
question.option_one = "4"
question.option_two = "5"
question.option_three = "6"

# Lưu đối tượng vào cơ sở dữ liệu
question.save()