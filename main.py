import uvicorn
if __name__ == '__main__':
    uvicorn.run("web:app", host="0.0.0.0", port=8001, reload=True,reload_excludes=['static','web_ui'])
    pass