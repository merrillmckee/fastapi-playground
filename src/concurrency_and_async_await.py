import app


@app.get('/')
async def read_results():
    results = await some_library()
    return results
