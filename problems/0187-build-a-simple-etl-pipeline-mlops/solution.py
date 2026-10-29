def run_etl(csv_text: str) -> list[tuple[str, float]]:
	t=[]
	l=[]
	c=0
	n=[]
	k = csv_text.split("\n")
	for i in k:
		j = i.split(",")
		if len(j)>2:
			if j[1].strip() == "purchase":
				try:
					float(j[2].strip())
					t.append(i)
				except:
					continue
	for k in t:
		p=k.split(",")
		l.append(p[0].strip())
	m=sorted(set(l))
	for i in m:
		for k in t:
			p=k.split(",")
			if p[0].strip()==i:
				c += float(p[2])
		n.append((i,c))
		c=0
	return n