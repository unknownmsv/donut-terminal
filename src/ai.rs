use reqwest::Client;
use serde_json::Value;

pub async fn ask_ai(prompt: &str) -> String {
    let url = "http://localhost:8080/proxy/ollama";
    let client = Client::new();
    let res = client.post(url)
        .json(&serde_json::json!({ "prompt": prompt }))
        .send()
        .await;

    match res {
        Ok(resp) => {
            if let Ok(json) = resp.json::<Value>().await {
                if let Some(content) = json.get("message").and_then(|m| m.get("content")) {
                    return content.to_string();
                }
            }
            "No response from AI".into()
        }
        Err(e) => format!("[!] Error contacting AI: {}", e),
    }
}
