import hashlib
import random
import time
import os
import threading

def brute_force_attack(filename, password_length):
  """
  Dosyanın şifresini brute force saldırısı ile çözer.

  Args:
    filename: Şifrelenecek dosya.
    password_length: Şifrenin uzunluğu.

  Returns:
    Şifre veya None.
  """

  start_time = time.time()

  # Dosyanın var olup olmadığını kontrol edin.
  if not os.path.exists(filename):
    raise FileNotFoundError("Dosya bulunamadı: {}".format(filename))

  # Dosya yolunu Windows'un tüm sürümlerinde desteklenen bir dizin oluşturma yöntemi kullanarak oluşturun.
  path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

  password = ""
  for i in range(password_length):
    password += chr(random.randint(ord("a"), ord("z")))

  while not is_valid_password(path, password):
    password += chr(random.randint(ord("a"), ord("z")))

  end_time = time.time()

  return password, end_time - start_time

def is_valid_password(filename, password):
  """
  Dosyanın şifresinin geçerli olup olmadığını kontrol eder.

  Args:
    filename: Şifrelenecek dosya.
    password: Şifre.

  Returns:
    Doğruysa True, değilse False.
  """

  # Dosya yolunu Windows'un tüm sürümlerinde desteklenen bir dizin oluşturma yöntemi kullanarak oluşturun.
  path = os.path.join(os.path.dirname(os.path.realpath(__file__)), filename)

  with open(path, "rb") as f:
    data = f.read()

  hashed_data = hashlib.sha256(data).hexdigest()

  return hashed_data == hashlib.sha256(password.encode()).hexdigest()

def main():
  """
  Ana fonksiyon.
  """

  # Dosyaları taramak için Windows'un tüm sürümlerinde desteklenen bir dizin oluşturma yöntemi kullanın.
  for root, dirs, files in os.walk(os.path.dirname(os.path.realpath(__file__))):
    for file in files:
      # Dosya uzantısı `.enc` olan dosyaları çözmek için Windows'un tüm sürümlerinde desteklenen bir yöntem kullanın.
      if file.endswith(".enc"):
        # Çözülen dosyaları yazdırmak için Windows'un tüm sürümlerinde desteklenen bir yöntem kullanın.
        password, time_taken = brute_force_attack(os.path.join(root, file), 10)
        if password is not None:
          print("Dosya bulundu:", os.path.join(root, file))
          print("Şifre:", password)
          print("Geçen süre:", time_taken)

if __name__ == "__main__":
  # exe dosyası olarak çıkarmak için Windows'un tüm sürümlerinde desteklenen bir yöntem kullanın.
  import pyinstaller
  pyinstaller.run(["brute_force.py", "--onefile", "--windowed", "--multiprocessing"])