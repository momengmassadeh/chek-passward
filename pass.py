# -*- coding: utf-8 -*-
"""
Created on Sat May 10 20:15:51 2025

@author: User
"""

import re

def check_password_strength(password):
    length_error = len(password) < 8
    lowercase_error = re.search(r"[a-z]", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    digit_error = re.search(r"\d", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    score = 5 - sum([length_error, lowercase_error, uppercase_error, digit_error, symbol_error])

    if score == 5:
        strength = "قوية جدًا"
    elif score >= 4:
        strength = "قوية"
    elif score >= 3:
        strength = "متوسطة"
    else:
        strength = "ضعيفة"

    print(f"\n🔐 قوة كلمة المرور: {strength}")
    print("تحليل:")
    if length_error:
        print("- ❌ الطول أقل من 8 حروف.")
    else:
        print("- ✅ الطول مناسب.")
    if lowercase_error:
        print("- ❌ لا تحتوي على أحرف صغيرة.")
    else:
        print("- ✅ تحتوي على أحرف صغيرة.")
    if uppercase_error:
        print("- ❌ لا تحتوي على أحرف كبيرة.")
    else:
        print("- ✅ تحتوي على أحرف كبيرة.")
    if digit_error:
        print("- ❌ لا تحتوي على أرقام.")
    else:
        print("- ✅ تحتوي على أرقام.")
    if symbol_error:
        print("- ❌ لا تحتوي على رموز خاصة.")
    else:
        print("- ✅ تحتوي على رموز خاصة.")

# تجربة
if __name__ == "__main__":
    pwd = input("🔑 أدخل كلمة المرور لاختبار قوتها: ")
    check_password_strength(pwd)