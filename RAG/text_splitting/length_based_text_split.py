from langchain_text_splitters import CharacterTextSplitter

text='''
Artificial Intelligence (AI) is one of the most transformative technologies of the modern era, reshaping how humans live, work, and interact with the world. At its core, AI refers to computer systems designed to perform tasks that normally require human intelligence, such as learning from data, recognizing patterns, understanding language, and making decisions. From everyday applications like voice assistants, recommendation systems, and facial recognition to advanced uses in healthcare, finance, transportation, and scientific research, AI has become deeply embedded in our daily lives. In healthcare, AI helps doctors detect diseases earlier, analyze medical images, and personalize treatment plans. In business, it improves efficiency by automating repetitive tasks, optimizing supply chains, and enabling data-driven decision-making. AI also plays a key role in emerging fields such as autonomous vehicles, robotics, and smart cities, where it enhances safety and operational accuracy. However, along with its benefits, AI raises important ethical and social concerns, including data privacy, algorithmic bias, job displacement, and the need for responsible governance. Addressing these challenges requires transparent systems, skilled professionals, and thoughtful regulations. When developed and used responsibly, AI has the potential to drive innovation, solve complex global problems, and significantly improve the quality of human life.
'''

splitter=CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)
result=splitter.split_text(text)
print(result)
print(result[0])