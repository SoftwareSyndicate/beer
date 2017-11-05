from flask import request, current_app, redirect, json
import urllib
import asyncio
import websockets

from aiohttp import web
import socketio

def connect():
    sio = socketio.AsyncServer()
    app = web.Application()
    sio.attach(app)

    
@sio.on('connect', namespace='/chat')
def connect(sid, environ):
    print("connect ", sid)

@sio.on('chat message', namespace='/chat')
async def message(sid, data):
    print("message ", data)
    await sio.emit('reply', room=sid)

@sio.on('disconnect', namespace='/chat')
def disconnect(sid):
    print('disconnect ', sid)

app.router.add_static('/static', 'static')
app.router.add_get('/', index)

if __name__ == '__main__':
    web.run_app(app)


