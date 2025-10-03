# -*- coding: utf-8 -*-
"""
主控台內在人格原型測驗

這個程式碼在主控台 (Terminal) 中運行，透過文字輸入/輸出
模擬原網頁應用程式的心理測驗邏輯。
"""

import sys

# --- 測驗數據結構 ---
# 格式: (選項文字, 對應的分數鍵)
questions = [
    {
        "text": "Q1: 面對一個新的挑戰或機會時，你的第一反應是？",
        "options": [
            ("1. 感到興奮，迫不及待地想親身體驗和嘗試。", 'A'),
            ("2. 仔細評估風險，尋求可靠的資訊或既有規範。", 'B'),
            ("3. 分析問題的本質，思考是否能用更有效率的方式完成。", 'C')
        ]
    },
    {
        "text": "Q2: 閒暇時，你最喜歡做什麼？",
        "options": [
            ("1. 戶外活動、即興旅行或參與任何能帶來新鮮刺激的事物。", 'A'),
            ("2. 與家人朋友共度時光，在熟悉、舒適的環境中放鬆。", 'B'),
            ("3. 閱讀、學習一項新技能，或專注於一個個人研究項目。", 'C')
        ]
    },
    {
        "text": "Q3: 你的朋友通常會如何形容你？",
        "options": [
            ("1. 活潑、無拘無束、充滿熱情和好奇心。", 'A'),
            ("2. 可靠、有責任感、重視承諾和穩定。", 'B'),
            ("3. 有創意、思想深刻、喜歡質疑現狀。", 'C')
        ]
    },
    {
        "text": "Q4: 對於一個重要的決定，你更依賴？",
        "options": [
            ("1. 你的直覺和當下的感覺，相信身體的反應。", 'A'),
            ("2. 過去的成功經驗和既定的社會價值觀。", 'B'),
            ("3. 理性分析、邏輯推理和數據支持。", 'C')
        ]
    },
    {
        "text": "Q5: 你認為人生的主要目標是？",
        "options": [
            ("1. 體驗生活的全部可能性，並隨時準備好改變方向。", 'A'),
            ("2. 確保自己和所愛的人擁有安全、穩定和和諧的生活。", 'B'),
            ("3. 創造一些有意義或改變世界的事物，留下影響。", 'C')
        ]
    }
]

# --- 測驗結果定義 ---
results = {
    'A': {
        "title": "🌳 探險家 (The Explorer)",
        "description": "你的內在核心是自由與體驗。你充滿好奇心，渴望探索未知，不喜歡被規則束縛。你活在當下，享受即興的樂趣，並相信生活最大的價值在於不斷的變動和個人的成長。你可能是團隊中的創新者和氣氛帶動者。"
    },
    'B': {
        "title": "🛡️ 守護者 (The Guardian)",
        "description": "你的內在核心是穩定與責任。你忠誠、可靠、腳踏實地，重視秩序和傳統。你總是為家人、朋友或社群提供堅實的後盾，你的行為準則基於實用性和對他人的關懷。你可能是團隊中不可或缺的基石和支持者。"
    },
    'C': {
        "title": "💡 創新者 (The Innovator)",
        "description": "你的內在核心是知識與變革。你是一個思想深刻的分析家，熱衷於解構事物並重塑它們。你不僅追求知識，更追求智慧，總是在尋找新的視角和更優雅的解決方案。你可能是團隊中的策略家和遠見者。"
    }
}

def run_quiz():
    """
    執行主控台版本的心理測驗。
    """
    # 初始化分數：A, B, C 分別計數
    score = {'A': 0, 'B': 0, 'C': 0}
    
    print("=" * 40)
    print("      內在人格原型測驗 - 主控台版")
    print("=" * 40)
    print("請輸入對應選項的數字 (1, 2, 或 3) 並按下 Enter。\n")

    for i, q in enumerate(questions):
        print(f"--- 問題 {i + 1}/{len(questions)} ---")
        print(f"{q['text']}")
        
        # 顯示選項
        for text, _ in q['options']:
            print(f"  {text}")
        
        # 獲取使用者輸入
        while True:
            try:
                user_input = input("你的選擇 (1, 2, 或 3): ").strip()
                choice_index = int(user_input) - 1
                
                if 0 <= choice_index < len(q['options']):
                    # 獲取分數鍵 (Score Key)
                    score_key = q['options'][choice_index][1]
                    score[score_key] += 1
                    print("-" * 10)
                    break
                else:
                    print("輸入錯誤，請輸入 1, 2, 或 3。")
            except ValueError:
                print("無效的輸入。請輸入數字。")
            except EOFError:
                # 處理終端機意外關閉
                sys.exit(0)


    # --- 顯示結果 ---
    print("\n" * 2)
    print("=" * 40)
    print("          測驗結果揭曉！")
    print("=" * 40)

    # 找出得分最高的類型
    max_score = -1
    result_key = ''
    
    # 處理平分情況：保留原網頁的優先順序 A > C > B 
    ordered_keys = ['A', 'C', 'B'] 

    for key in ordered_keys:
        if score[key] > max_score:
            max_score = score[key]
            result_key = key
        # 如果分數相等，由於我們是依序遍歷，A (探險家) 會優先於 B, C

    if not result_key:
         result_key = 'A' # 預設結果

    final_result = results[result_key]

    print(f"\n你的內在人格原型是：{final_result['title']}")
    print("-" * 30)
    print(final_result['description'])
    print("-" * 30)
    print(f"你的分數分佈: 探險家(A): {score['A']}, 守護者(B): {score['B']}, 創新者(C): {score['C']}")

if __name__ == "__main__":
    run_quiz()
