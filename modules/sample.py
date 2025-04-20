"""
🔼 This file is just for dry run purpose , nothing significant to project. 
"""
from exporter import generate_pdf
from transformers import pipeline
import matplotlib.pyplot as plt
import json
from summarizer import generate_summary
import re
 
test_transcript = """
for you. Yeah, that works for me. Yeah. Great. Okay. I see Rickel's starting things so we'll get going here in just one minute. Hi and welcome everyone. I'm Kim Hansen, Executive Director at Diabetes Canada and I'm really pleased to be here today to speak with you about how those of you who are affected by diabetes. Maybe either living with diabetes or with pre-diabetes or who have family members or are caring for those who do can live well with diabetes and reduce its risks. I'm so pleased today to be joined by endocrinologist and expert speaker Dr. Calvin Key. Dr. Key, thank you so much for being with us today. Welcome. Thank you. Really happy to be able to take part today. We'll be offering today's webinar in both English and Cantonese. We'll be answering some key questions around what diabetes is factors including ethnicity that can put some people at higher risk of developing type 2 diabetes, common signs and symptoms and how you can live well with diabetes. We'll be recording today's remarks so you can revisit them if you'd like on our YouTube channel and we'll be taking questions from our viewers. So if you've got any questions along the way, please don't hesitate to send them to us. If you're joining us by Zoom, you can use the Q&A function and if you're joining us on Facebook, please just include your questions in the comments and we'll get to them during the hour. So let's start by testing the knowledge of our viewers or sorry, actually we're going to first ask Dr. Key. Diabetes is a serious disease and it affects many, many Canadians talk to us about that. How many Canadians are we talking about here? Yeah, so diabetes is a very serious disease. I'm about 11 million Canadians currently either have diabetes or pre diabetes. So this represents one in four Canadians of the 11 million over 4.2 million are living with diabetes and over 6 million are at risk of developing diabetes. So every three minutes, one Canadian is diagnosed with diabetes by 2025, 13.6 million Canadians will either have diabetes or pre diabetes if we don't take steps to prevent and slow it's onset. So from these numbers, we can see why it's really important to learn about diabetes so that we can prevent it's onset and it's serious complications. So in terms of diabetes prevalence in Canada about 9.5% of the total population has been diagnosed with either type 1 or type 2 diabetes. The overall estimated prevalence of diabetes in Canada, including those cases that are undiagnosed, is expected to be around 28.5% of the population. So the prevalence of diabetes varies by region as well with new brands for having the highest rate of prevalence at 12.5% and new to it with the lowest at 3.9%. So I'm just going to go through that again for our Cantonese listeners to the work tonight. The average average is 1,100,000,000 people are living with diabetes and new to it with diabetes. The average average is 1,100,000 people are living with diabetes and new to it with diabetes. So the average average is 1,100,000 people are living with diabetes and new to it with diabetes. So the average average is 1,100,000 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So the average average is 1,100 people are living with diabetes and new to it with diabetes. So some of these, one of these statements is true rather, is it true that eating too much sugar causes diabetes? Is it true that insulin is a cure for diabetes? Is it true that diabetes is a serious disease like cancer or heart disease? Or is it true that there are two types of diabetes? And I'll invite you guys to play along on your own and you can score yourselves for kind of bragging rights with your friends and family. But we'll take the answers up quickly in the interests of time. So the answers are the true one here is that diabetes is a serious disease like cancer or heart disease. And Dr. Keys, we're going to talk to us today about some of the complications of diabetes and a bit more about why it's so serious. So we're going to talk to you about some of these things here that eating sugar causes diabetes. Oh, we know that a healthy diet is an important part of preventing or delaying type 2 where that's possible and helping all of us live Healthfully eating sugar doesn't make you get diabetes. Insulin is also not a cure for diabetes. Well, it's a really valuable life-saving treatment for people with many forms of diabetes. And we still have it. And finally, there are more than two types of diabetes and I believe Dr. Keys going to tell us all about that in just a few minutes. So let's dive in. Dr. Key, can you explain to us what kinds of changes happen in our body when we develop diabetes? Yeah, so what is diabetes? Let's often say that people are wondering. So our body gets energy by converting carbohydrates into glucose or sugar. We get carbohydrates from eating foods like breads, pasta, potatoes, milk, fruits and vegetables. And to use this glucose or energy, the body needs insulin. Insulin is like a key that lets glucose in from the bloodstream to enter the parts of the body that need it for energy. Insulin is a hormone that's made by your pancreas. And in someone with diabetes, the process of producing or using insulin is impaired. So now we'll talk about protein field. We have about 800おい bottles, meat high, comunidad cooked so far. We work early withλέ�iness of vitamin Nunden. And other said the cereals,ост sponges, tear them up and melt them down. In this case, I won theragen Calupuncture operation. I'm withelia. For him to use theseuateal hands, it can be adapted to aspray, but for a use of hypha due to the newborn pushi hearing. The rest im below theSa T the other side. either from noble or conscientious people, with minorities or drifting Carolesian people, with Indian clashes, and such, so they can make it these language necessarily for you. So then when diabetes sets in, Dr. Kei, what happens and what's the difference? So in a person who has diabetes, either their body makes no insulin and that would be type 1 diabetes. Or their body makes too little insulin or doesn't properly use the insulin that makes and that would be classified as type 2 diabetes. If there isn't enough insulin or the insulin is not working well, blood glucose levels, also known as blood sugar levels, become too high because instead of going to where it's needed for energy, the glucose sits in the bloodstream. High glucose levels make a person feel tired, thirsty, or need to urinate a lot. So a person might also lose a lot of weight very quickly. Have trouble seeing well or have infections more often. Over time, high glucose levels can cause damage to blood vessels and lead to serious and deadly complications. shade Plus is growing easier for a patient than saying something. Blend sunflower memory if you go numb or resistant. The specimen well, blood, SIM and healthIA type does only for absignhip heroes. However essential, one wouldests would choose to stop a rock while boarding ends up with a collaborating hospital. tree soil and the other would take clear that aischap called res spindell 초등اء Camelacharin and won't stop it twice in a row. background While this็ To what extent I would soon like to see the English language in English. I would soon like to hear the English language, but I would like to see the English language. Great. So, Dr. Ki, you've mentioned a couple of the types of diabetes, but could you just tell us a bit more about them and what the differences are among them? Sure, so let's start with type 1 diabetes. Type 1 diabetes is caused when the body can no longer make its own insulin. About 10% of people with diabetes have type 1. It's diagnosed most often in children and young adults. And people with type 1 must inject insulin every day. Let's just be done in several ways, get it through needles, insulin pens or with an insulin pump. Type 1 diabetes cannot be prevented, and currently there's no cure. However, it can be managed with healthy eating, exercise, glucose testing, and daily insulin injections. So, let's talk about 1 young type 1. 1 young type is because of the disease, the disease is not the case with the disease that is in the brain. But the disease is about 10% of the disease. The second time in the world, the disease is about 10% of the disease. This disease is because of the disease that is in the brain. The disease is about 3% of the disease. The first is to use the disease to reduce the disease. The first is to reduce the disease to reduce the disease. The first is to reduce the disease to reduce the disease. But the first is to reduce the disease. The first is to reduce the disease to reduce the disease. So, we'll move on to 3 diabetes. So, 3 diabetes is when your blood glucose levels are higher than normal, but below the level to be diagnosed with diabetes. So, if you found that category, you might be told that you have pre-diabetes. Although there is no cure for diabetes, and the longer you have diabetes, the higher the risk of complications. Pre-diabetes offers a warning. It gives you a chance to take action to prevent type 2 diabetes and the same or healthy. If you have pre-diabetes, type 2 diabetes can be prevented, or delayed, the lifestyle choices such as eating healthy and exercising regularly. Pre-diabetes can be diagnosed by your healthcare professional with a routine blood test. 10. KTong Liu Bang You've got a lot of pain in your stomach, but you have to be a healthy one. You would be to go spend time on chances to ACTants. One year, a ayyyy cholerahn activity suggests that kidney cav aquele eschon such as assessed分鐘 od Sparkham whereas Q além But through less mortality, finally you can go to the mainland along the way. When we first found a new network on the Kija Lake, we found a large number of seafood at the hands of these Changes. We will try, diabetes. So this is the most common form of diabetes, about 90% of people with diabetes have type 2. In type 2 diabetes, this is most commonly seen in adults, but there has been an increasing trend in young people developing type 2 as well, especially among the indigenous population and also amongst South Asian populations as well in Canada. So here recall, type 2 diabetes is caused when the body cannot make enough insulin or it can't properly use the insulin that it does make. While there's currently no cure for type 2 diabetes, it may be prevented or delayed with healthy eating exercise and checking your blood sugar as well as taking your medications. You got out of the Gong Ha Yi Yan Kong Li Feng. Yi Yan Kong Li Feng in the world. In 1990 the Chinese warrior 16 came to mark his biological life. I believe that was my biological complex. rabbit room were softens, Toozi, I don't know if that music could be made with C5 or permanent Arts Word like a rock. Thus, the anime I aucune mentioned is ascat and NO played character. Yav Matlan, Gian Hong Yamsik, Wang Dong, Kup Ginshat, Hong, Hu Tong, Le Yu Fang, Watzai Ginsi, Bensing. So we're going to move on to talk about gestational diabetes now. It's recommended that all pregnant women be tested for gestational diabetes. It affects about 3.7% of all pregnancies. Risk associated with gestational diabetes include having a very large baby, which can be dangerous for both women baby during the delivery. Higher rates of cesarean delivery, so when the baby is delivered, we are an incision made that the mother's abdomen and uterus, also known as a sea section, and dangerously full blood sugar levels for the baby. However, it can be managed by making healthy food choices and sometimes with insulin. After pregnancy, among the blood sugar levels, almost often returns back to normal. Although, among the blood sugar levels, often returned to normal after pregnancy, they are at a greater risk of developing type 2 diabetes later on in life. Yav Yamsik, Hong Li Feng, Yav Yibo, Fak Yu Fang, Yamsik, Hong Li Feng, this virus wakes up. Fatherrd Deng grenade gene, and this in so many years, should be destroyed. Grinding healthcare, skincare and smells of drugs are noworter than drug use card of mages. as the country speaks a lot, the advocacy of the Japanese explained culture Zeyu Tang The forming of the jet plane Giao Kou We could deep remove the color of data and let's say, if Wisssey talks about ice closing the world So that is it, not a stand picture of the flagship in furnishing but the mlying mail was made for a smaller batteryé and the E A That's a lot of fantastic information, Dr. Key. Thank you so much. So tell us a little bit more about what some of the risk factors are for type 2 diabetes. Yeah, sure. So the risk factors for developing type 2 diabetes include age. So if you're over 40 years of age, your risk is higher. Second is family history. If you have a first degree blood relative with type 2 diabetes, for example, a parent, a brother, or a sister, your risk will be higher. Ethnic background. If you're indigenous, if you're Asian, especially South Asian, or if you're Hispanic, or African, your risk will be higher. If you've had gestational diabetes, or if you've given birth to a baby that weighed over 9 pounds, or 4 kilograms, or if you've had polycystic ovarian syndrome, your risk will be higher. Black of exercise. So there's a strong link to type 2 diabetes for people who don't exercise, as well as being overweight. Another strong risk factor for type 2 diabetes, especially where weight is mostly around the stomach or apple shaped. You can lower your risk by being fit and by making healthy food choices. The last risk factor is having high blood pressure or high cholesterol. Come here. Let's talk about the second risk factor of the disease. First, it's a link. If you're a 40-year-old, the risk factor of the disease is high. If you're a healthy, healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. If you're a healthy, or healthy, or healthy, or healthy, the risk factor of the disease is high. Great. Thank you for that, Dr. Key. Now, before we go to the next slide, one of our viewers has a great question. Our viewer recently had a high sugar content in a urine sample. Does that mean that they have diabetes? They're going for blood work on the 14th of August to find out. But I imagine our curious in the meantime. So currently, we don't diagnose diabetes by looking at the urine. Although the name diabetes notes, actually does refer to sweet urine. It's a finding that people have noticed for hundreds of years. So while that certainly could mean that they might have diabetes, on the standard way of diagnosing diabetes, would be through blood tests. So you could speak to your doctor, about getting the proper blood tests to get the diagnosis of diabetes. Good advice. Thank you. So let's move on then. What are some of the signs and symptoms that you a person might have diabetes that we should be watching for? Sure. Sure. So some of the signs and symptoms, the most common signs that we should be aware of are the need to urinate often, the unusually thirsty, a change in weight, being very tired, blurry vision, with type 1 diabetes, the symptoms tend to progress very quickly, and can be quite dramatic. Although with type 2 diabetes, the symptoms usually progress more slowly, and they actually go unnoticed. Many people who don't know they have type 2 diabetes, may not notice the symptoms at all. In fact, only one out of every three people that have diabetes, in fact, one out of every three people that have diabetes actually don't know that they have it. So that's why regular testing for diabetes is important, especially if you have the risk factors that we talked about. And also please remember that risk assessments, and testing for diabetes are actually two different things. Testing for diabetes involves a simple blood test that doesn't cost much. You should get tested every three years from age 40 onwards. If you have other risk factors, then you should get tested before the age of 40 or every year. So talk to your doctor about getting tested for diabetes. Let me know how to go on hot, thanks, and the symptoms. First, we need to get a little bit more. In the morning, the doctor said that the patient doesn't have a doctor. He said that he would get tested for diabetes. He said that he would get tested for diabetes. He said that he would get tested for diabetes. He said that he would get tested for diabetes. He said that he would get tested for diabetes. He said that he would get tested for diabetes. He said that he would get tested for diabetes. He said that he would get tested for diabetes. He said that he would get tested for diabetes. So, we need to get rid of the blood test. He said that he would get tested for diabetes. He said that he would get tested for diabetes. The second is the second is the second is the second is the second is the second is the third is the third is the third is the third is the third is the third is the third is the third is earth� of tax吃 8 12 30�nty片 12 39 38 28 40 37 have strokes twice as often as those with high blood pressure alone, and the experience higher rates of adult blindness. Heart disease is two to four, two to four times more common in people with diabetes, and diabetes is the most common cause of kidney failure and amputation that isn't the result of an accident. However, there is good news. With proper diabetes management, these problems can be prevented or at least delayed. The same is the same as the other. The same is the same as the other. The same is the same as the other. The same is the same as the other. The same is the same as the other. The same is the same as the other. You can change your diabetes when you have heart disease with low blood pressure or low blood pressure caused紀品 toячy shed กاشibar Really good news that a medical diseases are So good news, Dr. Key, that we can prevent or delay the complications of diabetes that you've just described. What are some of the things that we can do in order to prevent or delay these? Absolutely. So let's start by talking about healthy food choices. Well, the person has diabetes or not, we only tell the year when we follow Canada's food guide. This guide can help people make healthy food choices and eating habits. Guide is now unabailable in Chinese as well as in Hindi and Gujarati and other languages. It's very important to make a habit to eat a variety of healthy foods each day. I have a plate that is diverse in his food types which draw some each of the food groups, fruits, vegetables, protein foods and whole grain foods. When making food choices, choose protein foods that come from plants more often. Choose foods with healthy fats instead of saturated fat. Healthy fats include olive, canola, soy bean and sunflower oil. Saturated fats include processed meats like sausages and deli meats. Limit highly processed foods. If you choose these foods, eat them less often and in smaller amounts. Prepare meals and snacks using ingredients that have little to know added sodium, sugars or saturated fat. Choose healthier menu options when eating out and make water the drink of choice. Replace sugary drinks with water that includes juice, use food labels. And be aware that food marketing can influence your choices. The next is the Heng Sikma Sunsang, the next is the Heng Viu-Bang. We will prepare담 Kimchi as in for theci können, the whole thing of a seul dish is used. Now, we have Niren Kimchi and takenutral哦 to eat chicken荷 recipes. Beef<|bo|>, meaty green onion and A bener walk the pillar of the ferv będzie씩úde. In a separate trail, we will not train in the correct trail, just legways, just sit down, eat and cook deliciously. The journey through the cal�iscoat leaders, either one could go around online, or for great supplies. Just outside the mood for convenience. and the other side of the house, We allow them to be organized! Reduce the槍 or belt. We replace the Gundam Help and Safety supplies as well as export with weapons. I'd just click on the crown number button for mí-up the faithful German soldiers. Adds two small demanded procedures for the work of the soldier, including Carbonated Catalan Baguaredunt COME and vending machine. The Eli Palm Bay tree leaves, a red-� llon glaze area and red wire and 이제m Tatha a sweet rug. here are the delicious meals possible for someья dace Go to watch all the dishes dinner See you so far, we're young on the issues. Fantastic tips, Dr. Keith, thank you. Now let's put our viewers on the hot seat again and we'll test their knowledge about healthy eating. So out of these statements, one of them is true. And see if you can determine which one it is. Is it true that eating health only means that you can't eat chocolate? Is it true that healthy food choices mean eating foods that have no flavor? Is it true that healthy eating means only eating fresh fruits and vegetables? And what about unsweetened juice has sugar? Which of those is true? So the answer might surprise you. The true answer there is that unsweetened juice has sugar. It is a natural form of sugar, but it is sugar nonetheless and it can act similarly in our bloodstreams to refined sugars. So it's good to consume juice in moderation if at all, water should still be our beverage of choice. Eating healthily can include eating chocolate, especially dark chocolate that can have some other health benefits as long as we eat it in moderation. Eating healthily, most certainly does not mean foods that have no flavor for its vegetables can be very, very delicious. And healthy eating does not mean only eating fresh fruits and vegetables because frozen and canned vegetables can be equally nutritious and sometimes a very convenient way of making sure we fill half of our plates with fruits and vegetables that every meal. Great. So let's turn it back over to our expert Dr. Key. What else can we do? Or it's sorry, it's not just about what we eat is it? It's really also about how we would you say? Yeah, so it's really important to know that healthy eating is more than the foods that you eat. It's about where, when, why, and how you eat. So be mindful of your eating habits. Take time to eat. Notice when you're hungry and when you're full. Cook more often. Plan what you eat. Involve others in planning and preparing meals. And I think certainly everyone's doing more cooking nowadays. Enjoy your food. Culture and food traditions can be part of healthy eating. Eat meals with others. For more information on these and other recommendations, Candidate's Food Guide is accessible online. Whether you have diabetes or not, when we all eat healthier, we can do that by following Candidate's Food Guide. Eating well with Candidate's Food Guide can help you to make healthy choices. It lists the number of servings that you need to get all the nutrients your body needs to be healthy. And you can easily access this information online with a better question to the bacteria. Between the food ingredients are such a essential ingredient for our energy. Hé, how they were meant, can be added inamerica, and elsewhere in snack conditions, to the average in which beer you have to cook, but you can easily see how it Tropical Gasping perching the properties in the area. Especially overnightDEestone. There's a lot shopping left. We're going out to pool food as well. Today we'll have can afford to make healthy they tastes well. How to Bans Lake? My friend said some of my colleagues heard got me. What kind of a man wants to drink water? And how to drink some water. Theseil, how do we make it water? Good luck, friend. They can drink this! So great tips on how we can eat healthily but I'm guessing that exercise is also an an important part of protecting ourselves against the risk of developing type 2 diabetes or the complications of diabetes. How can we incorporate physical activity into our daily livestock key? So almost everyone, whether or not they have diabetes, will benefit from regular exercise. If you're just starting to get active, talk with your healthcare professional about how to get started. It's best to avoid prolonged sitting, try to interrupt sitting time by getting up briefly every 20 to 30 minutes. The goal is to add 150 to 300 minutes of exercise every week. That sounds like a lot, but it's only about 20 minutes a day. You can add in some weightlifting exercises a couple times a week, an easy way to try lifting soup cans or some heavy books while you watch TV. And it starts slow and build up. Small changes will make a big difference. Some additional tips include parking the car further from the store, taking the stairs, walking your dog, playing actively with your kids, turning off the TV, computer or video games, and beginning with walking. I think it's a bit too much. I think it's more than a year, but I think it's a bit too much. Taking the feeling ofParvilleum, who wants to treat you with help. Every day they do well, each year they hear their technical music. You work my way to the first 30 minutes and for more than 30 minutes to arrive. 4 framework A machine Its ratio is further than 3-3 percent 20 per liter A total of 15 per liter In particular in each statement an ordinary Word Can strengthen the Contest The small area is big, but not big. The main area is the main area. The main area is the main area. The main area is the main area. The main area is the main area. The main area is the main area. The main area is the main area. If I may, I would like to take a couple of moments to tell our viewers how diabetes can do and I would like to help them. I wonder if you would mind just giving a brief summary of it. Some of the things that diabetes can do does to help those of us living with diabetes or at risk of it are that we fund research into ways to prevent, manage or cure diabetes. We advocate with the government and make recommendations to ensure that health and access to care, medications and devices are priorities for all levels of government in Canada. We support healthcare professionals by providing them with up-to-date information, education, research and the latest treatment methods for diabetes so that it helps to ensure that those of us with diabetes get the best care possible from our healthcare providers. We provide lots of information and educational resources for people with diabetes on our website, on our social media channels, on our YouTube channel. This webinar today is one example of that. You can also access our 1-800-BANTIN line to ask any questions that you might have about diabetes in general about financial supports that might be available to you through your local government. Or if you've got specific questions about your own health, we can connect you to a volunteer diabetes educator who can provide you with more customized advice so don't hesitate to reach out to us. The NTIN line. Fantastic. Dr. Keith, thank you so much. We're pretty much at the end of our time together today, but I really want to thank you, Dr. Keith, for sharing your knowledge and expertise with us. I think you've given us a lot of really helpful tips for how we can protect ourselves against either developing diabetes or its complications. So thank you. We want to thank our viewers and encourage them to reach out to diabetes Canada at any other ways that you can see on your screen just a reminder that this recording will be made available on diabetes Canada's YouTube channel if you want to go back and refer to any of the pieces of information we've shared. Before we wrap up, I'll just offer you Dr. Keith and closing remarks. So thank you so much for organizing this and I think it's a great initiative from diabetes Canada. I'd like to also thank Jennifer Yu for helping preparing some of the Chinese content and to encourage everyone to become more healthy and active and to be more aware about what diabetes is and what it means for all of us. Wonderful. Thank you so much, Dr. Keith and I wish you and everyone else a good long weekend. And please be well.

"""


def format_transcript(raw_transcript: str) -> str:
    """
    Format a raw transcript to make it more suitable for LLM processing.
    This helps prevent hallucinations and empty arrays.
    """
    import re

    # If transcript is already well-structured, don't modify it
    if "\n\n" in raw_transcript and len(raw_transcript.split("\n")) > 5:
        return raw_transcript

    # Step 1: Try to detect if this is a single-line or poorly formatted transcript
    if raw_transcript.count("\n") < raw_transcript.count(". ") / 3:
        print("Detected single-line or poorly formatted transcript. Reformatting...")

        # Step 2: Split on potential speaker indicators
        # Common patterns like "Person:", "John:", "[John]:", "Speaker 1:" etc.
        speaker_pattern = r'(?:\n|^|\. )([A-Z][a-zA-Z\s]*|\[[^\]]+\]|Speaker\s*\d+):[ \t]'

        formatted = raw_transcript

        # If we detect speaker patterns, split on them
        if re.search(speaker_pattern, raw_transcript):
            formatted = re.sub(speaker_pattern, r'\n\n\1: ', formatted)
        else:
            # If no speaker patterns, try to split on sentences
            formatted = re.sub(r'\.(\s)', r'.\n\n', formatted)

        # Ensure consistent newlines
        formatted = re.sub(r'\n{3,}', '\n\n', formatted)

        # Clean up any trailing whitespace
        formatted = re.sub(r' +$', '', formatted, flags=re.MULTILINE)

        # print(f"Reformatted transcript from {raw_transcript.count('\n')} to {formatted.count('\n')} line breaks")
        return formatted

    return raw_transcript


new_transcript = format_transcript(test_transcript)

# Test the summarizer
summary = generate_summary(new_transcript)

# Print the results
print(json.dumps(summary, indent=2))

sentiment_pipeline = pipeline(
    "sentiment-analysis", model="nlptown/bert-base-multilingual-uncased-sentiment")

# Chunk the transcript (every 5 sentences)


def chunk_transcript(transcript, chunk_size=5):
    sentences = re.split(r'(?<=[.?!])\s+', transcript.strip())
    return [' '.join(sentences[i:i+chunk_size]) for i in range(0, len(sentences), chunk_size)]


chunks = chunk_transcript(new_transcript)
sentiments = [sentiment_pipeline(chunk)[0] for chunk in chunks]

# Map labels to scores


def label_to_score(label):
    try:
        stars = int(label[0])
        return stars
    except:
        return 3  # neutral fallback


scores = [label_to_score(s['label']) for s in sentiments]

# ---------------------------
# Step 4: Generate Timeline Chart
# ---------------------------


def map_score_to_emoji(score: float) -> str:
    if score <= 1.5:
        return "😢"
    elif score <= 2.5:
        return "🙁"
    elif score <= 3.5:
        return "😐"
    elif score <= 4.5:
        return "🙂"
    else:
        return "😄"


def plot_sentiment_timeline(scores, chunk_duration_secs=30):
    """
    Enhanced sentiment timeline plot with emojis and time intervals on x-axis.
    """
    import matplotlib.pyplot as plt

    x = list(range(len(scores)))
    y = scores

    # Time labels (e.g. 0:00, 0:30, 1:00, etc.)
    time_labels = []
    for i in x:
        total_secs = i * chunk_duration_secs
        mins = total_secs // 60
        secs = total_secs % 60
        time_labels.append(f"{mins}:{secs:02d}")

    # Emojis mapped from score
    emoji_labels = [map_score_to_emoji(score) for score in y]

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, marker='o', color='blue', linewidth=2)

    # Add emoji text above each point
    for i, (xi, yi) in enumerate(zip(x, y)):
        plt.text(xi, yi + 0.2, emoji_labels[i], ha='center', fontsize=16)

    plt.title("Sentiment Timeline (1=Negative, 5=Positive)")
    plt.xlabel("Approximate Time")
    plt.ylabel("Sentiment Score")
    plt.xticks(ticks=x, labels=time_labels, rotation=45)
    plt.yticks(range(1, 6))  # sentiment scores range
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("sentiment_timeline.png")
    plt.close()
    print("✅ Enhanced sentiment timeline saved as 'sentiment_timeline.png'")


# # Load summarization pipeline for topic extraction
# topic_pipe = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

# # Generate a short topic/summary per chunk
# def get_chunk_topics(chunks):
#     topics = []
#     for chunk in chunks:
#         try:
#             summary = topic_pipe(chunk[:1024], max_length=10, min_length=2, do_sample=False)[0]['summary_text']
#             topics.append(summary.strip())
#         except:
#             topics.append("Unknown Topic")
#     return topics

# chunk_topics = get_chunk_topics(chunks)
# def generate_sentiment_shift_summary(scores, topics=None):
    labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]
    emojis = ["😢", "🙁", "😐", "🙂", "😄"]

    def label(score):
        if score <= 1.5: return 0
        elif score <= 2.5: return 1
        elif score <= 3.5: return 2
        elif score <= 4.5: return 3
        else: return 4

    shifts = []
    for i in range(1, len(scores)):
        prev, curr = label(scores[i-1]), label(scores[i])
        if abs(curr - prev) >= 1:
            topic = f"'{topics[i]}'" if topics and i < len(topics) else f"chunk {i}"
            shifts.append(f"Tone shifted from {labels[prev]} to {labels[curr]} {emojis[curr]} during {topic}.\n")

    if not shifts:
        return "Sentiment remained relatively consistent throughout the session. " + emojis[label(scores[0])]

    return " ".join(shifts)
# shift_summary = generate_sentiment_shift_summary(scores, chunk_topics)
# print("\n🧠 Sentiment Insight:\n", shift_summary)

# plot_sentiment_timeline(scores)

# pdf_path = generate_pdf("Ytesting", new_transcript, summary)
# print(pdf_path)
