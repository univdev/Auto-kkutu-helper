import os
from selenium import webdriver;
from guifw.appJar import gui

class KkutuHelper:
	words = {};
	alreadyWords = [];

	def turnOnKkutu(self):
	    binary = './chromedriver2'
	    browser = webdriver.Chrome(binary)

	def callFiles(self):
		# 디렉토리에 있는 파일을 읽어와서 배열에 넣고 긴 단어 순서대로 정리함.
		# 굳이 프로그램을 종료하고 켜지 않아도 이 메소드만 돌리면 파일을 다시 읽어옴.
		directory = 'answers';
		txtlist = os.listdir(directory);
		
		for filename in txtlist:
			context = open('{}/{}'.format(directory, filename), 'r', encoding="UTF-8").read().split('\n');

			for word in context:
				firstWord = word.strip()[0:1];
				if firstWord not in self.words:
					self.words[firstWord] = [];
				self.words[firstWord].append(word);

			for key, obj in self.words.items():
				self.words[key] = sorted(obj, key=lambda word: len(word), reverse=True)

	def callWord(self, start):
		# 시작 단어를 받으면 해당 배열에서 가장 긴 단어를 불러옴.
		if start not in self.words:
			return false;

		for word in self.words[start]:
			if word not in self.alreadyWords:
				self.alreadyWords.append(word);
				return word;

		return false;

	def answer(self):
		# 정답 제출
		# .jjo-display.ellipse (현재 시작 단어가 적혀있는 박스의 클래스)
		answer = self.callWord();

kh = KkutuHelper();

def layout():

	def btn(label):
		if label == '끄투 접속':
			kh.turnOnKkutu();
		elif label == '핵 작동':
			kh.answer();

	app = gui("Kkutu auto helper", '400x150');
	app.addLabel("description", "끄투온라인을 편하게 즐기기 위한 핵입니다.", 0, 0, 2);
	app.addButtons(["끄투 접속", "핵 작동"], btn, 1, 0, 2);

	return app;

layout().go();