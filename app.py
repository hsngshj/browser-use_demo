import json
from flask import Flask, render_template, request
from langchain_openai import ChatOpenAI
from browser_use import Agent
import asyncio
from dotenv import load_dotenv
import os

# .envファイルを読み込む
load_dotenv()

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    result_json_str = None
    result_content = None
    if request.method == 'POST':
        task = request.form['task'] + " 日本語で回答してください。"
        result = asyncio.run(run_agent(task))
                            
        # AgentHistoryListオブジェクトを辞書に変換
        if hasattr(result, 'to_dict'):
            result_json = result.to_dict()
        else:
            # カスタムシリアライザを使用
            result_json_str = json.dumps(result, default=lambda o: o.__dict__, indent=4, ensure_ascii=False)
            result_json = json.loads(result_json_str)  # 文字列を辞書に変換
        
        # extracted_contentを取得
        result_content = result_json['history'][-1]['result'][-1]['extracted_content']
        
    return render_template('index.html', result=result, result_json=result_json_str, result_content=result_content)

async def run_agent(task):
    agent = Agent(
        task=task,
        llm=ChatOpenAI(model="gpt-4o-mini", api_key=os.getenv("OPENAI_API_KEY")),
    )
    result = await agent.run()
    return result

if __name__ == '__main__':
    app.run(debug=True)