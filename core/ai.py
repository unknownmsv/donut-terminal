import requests
import json
from time import sleep

PROXY_AI_URL = "http://localhost:8080/proxy"
MAX_RETRIES = 3
RETRY_DELAY = 1  # seconds

def ask_ai(provider, prompt):
    """
    ارسال درخواست به پروکسی AI با ویژگی‌های:
    - تلاش مجدد خودکار
    - مدیریت خطاهای دقیق
    - پشتیبانی از چندین ساختار پاسخ
    """
    url = f"{PROXY_AI_URL}/{provider}"
    
    for attempt in range(MAX_RETRIES):
        try:
            response = requests.post(
                url,
                json={"prompt": prompt},
                headers={"Content-Type": "application/json"},
                timeout=30
            )
            
            if response.status_code != 200:
                raise requests.exceptions.RequestException(
                    f"Status {response.status_code}: {response.text}"
                )
                
            return parse_ai_response(response.json())
            
        except requests.exceptions.RequestException as e:
            if attempt < MAX_RETRIES - 1:
                sleep(RETRY_DELAY)
                continue
            return f"[!] خطای ارتباطی: {str(e)}"
        except json.JSONDecodeError:
            return "[!] پاسخ نامعتبر از سرور AI"
        except Exception as e:
            return f"[!] خطای غیرمنتظره: {str(e)}"

def parse_ai_response(data):
    """پارسر هوشمند برای پاسخ‌های AI"""
    if isinstance(data, str):
        return data
    
    # ساختار Ollama
    if "message" in data and isinstance(data["message"], dict):
        return data["message"].get("content", "پاسخی دریافت نشد")
    
    # ساختار OpenAI
    if "choices" in data and isinstance(data["choices"], list):
        if len(data["choices"]) > 0:
            choice = data["choices"][0]
            if "message" in choice and isinstance(choice["message"], dict):
                return choice["message"].get("content", "پاسخی دریافت نشد")
    
    # ساختار ساده
    if "response" in data:
        return data["response"]
    
    # حالت پیش‌فرض
    return str(data)