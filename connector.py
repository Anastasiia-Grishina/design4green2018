import sys, os
from flask import Flask, jsonify, request
import pymongo
from pymongo import MongoClient
from flask import Flask, jsonify, request
from datetime import datetime
from datetime import timedelta
import uuid
import dateutil.parser as parser
import hashlib

client = MongoClient('localhost', 27017)
mongo = client.greencoders

class Manager:
	def getBasicQuestions(self):
		data = mongo.questions
		query = {}
		#query[''] = ''
		questionList = {}
		i = 1 
		for q in data.find(query).sort('number',pymongo.ASCENDING):
			question = {}
			question['question'] = q['question']
			question['number'] = q['number']
			question['choice'] = q['choice']
			question['type'] = q['type']
			questionList['question'+str(i)] = question
			i = i + 1	
                #f = open("demofile.txt", "w")
                #f.write(str({'status':'success','result':questionList}))
                return jsonify({'status':'success','result':questionList})	

	def saveAllAnswers(self, answers):
		data = mongo.answers
		json = {}
		i = 0
		while i < len(answers):
			que = 'question'+str(i+1)
			json[que] = answers[i]
			i = i + 1
		print(json)
		if data.insert(json):
			return jsonify({'status':'success'})
		else:
			return jsonify({'status':'failed'})
