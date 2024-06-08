from flask import Flask, request, jsonify
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import pickle
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


# Load LeafName from the pickle file
with open('D:/Projects/MERNLEAF/flask/pythonScript/LeafName.pkl', 'rb') as file:
    LeafName = pickle.load(file)

# Load the pre-trained model
model = load_model('D:/Projects/MERNLEAF/flask/pythonScript/trained_model.h5')

leaf_uses = {
    'Aloevera-Aloe barbadensis': 'Used for its soothing and healing properties, commonly applied to burns and wounds.',
    'Amaranthus Green_Amaranthus viridis': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Amaranthus Red_Amaranthus tricolor': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Amla-Phyllanthus emlica Linn': 'Used in traditional medicine for its high vitamin C content and antioxidant properties.',
    'Amruta Balli-Tinospora cordifolia': 'Used in traditional medicine for its immune-boosting and anti-inflammatory properties.',
    'Arali-Nerium oleander': 'Used with caution in traditional medicine; toxic if ingested.',
    'Arive_Dantu_Amaranthus viridis': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Ashoka-Saraca asoca': 'Used in Ayurveda for treating gynecological disorders.',
    'Ashwagandha_Withania somnifera': 'Used in traditional medicine for its adaptogenic and stress-relieving properties.',
    'Asthma plant_Euphorbia hirta': 'Used in traditional medicine for treating respiratory conditions.',
    'Astma_weed': 'Used in traditional medicine for treating respiratory conditions.',
    'Avacado_Persea americana': 'Leaves used in traditional medicine for their digestive and anti-inflammatory properties.',
    'Avaram_Senna auriculata': 'Used in traditional medicine for its cooling and diuretic properties.',
    'Badipala': 'Likely a regional name; more information needed.',
    'Balloon vine_Cardiospermum halicacabum': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Bamboo-Bambusoideae': 'Young leaves used in traditional medicine and as fodder.',
    'Basale_Basella alba': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Beans-Vigna spp. (Genus) or Phaseolus spp. (Genus)': 'Leaves used as a leafy vegetable and in traditional medicine.',
    'Bellyache bush (Green)_Jatropha gossypiifolia': 'Used with caution in traditional medicine; toxic if ingested.',
    'Benghal dayflower_ Commelina benghalensis': 'Used in traditional medicine for its cooling properties.',
    'Betel-Piper betle': 'Leaves chewed for their stimulant effects and used in traditional medicine for their digestive properties.',
    'Betel_Nut_Areca catechu': 'Used with caution in traditional medicine; carcinogenic if consumed regularly.',
    'Big Caltrops_Tribulus terrestris': 'Used in traditional medicine for its diuretic properties.',
    'Black-Honey Shrub_Tribulus terrestris': 'Used in traditional medicine for its diuretic properties.',
    'Brahmi-Bacopa monnieri': 'Used in traditional medicine for its cognitive-enhancing properties.',
    'Bringaraja-Eclipta prostrata': 'Used in traditional medicine for its hair growth-promoting properties.',
    'Bristly Wild Grape_Cissus quadrangularis': 'Used in traditional medicine for its bone-healing properties.',
    'Butterfly Pea_Clitoria ternatea': 'Used in traditional medicine for its cognitive-enhancing and anti-anxiety properties.',
    'Camphor-Cinnamomum camphora': 'Leaves used in traditional medicine for their aromatic and analgesic properties.',
    'Cape Gooseberry_Physalis peruviana': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Cardiospermum halicacabum': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Caricature': 'Likely a regional name; more information needed.',
    'Castor-Ricinus communis': 'Leaves used in traditional medicine for their anti-inflammatory properties; toxic if ingested.',
    'Catharanthus': 'Used in traditional medicine and for producing anticancer compounds.',
    'Celery_Apium graveolens': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Chakte': 'Likely a regional name; more information needed.',
    'Chilly-Capsicum spp. (Genus)': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Chinese Spinach_Amaranthus dubius': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Citron lime (herelikai)-Citrus medica (Citron) or Citrus aurantiifolia (Lime)': 'Leaves used in traditional medicine for their aromatic and digestive properties.',
    'Coffee-Coffea spp. (Genus)': 'Leaves used in traditional medicine for their stimulant properties.',
    'Common Wireweed_Sida rhombifolia': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Common rue(naagdalli)-Ruta graveolens': 'Used in traditional medicine for its anti-inflammatory and antispasmodic properties.',
    'Coriander-Coriandrum sativum': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Country Mallow_Abutilon indicum': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Crown flower_Calotropis gigantea': 'Used in traditional medicine for its anti-inflammatory properties; toxic if ingested.',
    'Curry Leaf-Murraya koenigii': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Doddapatre-Plectranthus amboinicus': 'Used in traditional medicine for its digestive and respiratory properties.',
    'Drumstick-Moringa oleifera': 'Leaves used as a leafy vegetable and in traditional medicine for their nutritional and anti-inflammatory properties.',
    'Dwarf Copperleaf (Green)_Acalypha reptans': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Dwarf copperleaf (Red)_ Acalypha wilkesiana': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Ekka-Calotropis gigantea': 'Used in traditional medicine for its anti-inflammatory properties; toxic if ingested.',
    'Eucalyptus-Eucalyptus spp. (Genus)': 'Leaves used in traditional medicine for their antiseptic and respiratory benefits.',
    'False Amarnath_Digera muricata': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Fenugreek Leaves_ Trigonella foenum-graecum': 'Used in cooking and traditional medicine for their digestive properties.',
    'Ganigale': 'Likely a regional name; more information needed.',
    'Ganike-Solanum nigrum': 'Used in traditional medicine for its anti-inflammatory and analgesic properties.',
    'Gasagase-Grewia asiatica': 'Leaves used in traditional medicine for their cooling properties.',
    'Gauva-Psidium guajava': 'Leaves used in traditional medicine for their digestive and antimicrobial properties.',
    'Geranium_ Pelargonium spp. (Genus)': 'Used in traditional medicine for their aromatic and anti-inflammatory properties.',
    'Giant Pigweed_Amaranthus titan': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Ginger-Zingiber officinale': 'Leaves used in traditional medicine for their digestive and anti-inflammatory properties.',
    'Globe Amarnath-Gomphrena globosa': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Gongura_Hibiscus sabdariffa': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Green Chireta_Andrographis paniculata': 'Used in traditional medicine for its immune-boosting and anti-inflammatory properties.',
    'Henna-Lausonia inermis': 'Leaves used in traditional medicine for their cooling properties and for hair dye.',
    'Hibiscus-Hibiscus rosa sinensis': 'Leaves used in traditional medicine for their anti-inflammatory and hair care properties.',
    'Holy Basil_ Ocimum sanctum': 'Used in traditional medicine for its immune-boosting and anti-inflammatory properties.',
    'Honge-Milletia': 'Likely referring to Millettia pinnata; used in traditional medicine for its anti-inflammatory properties.',
    'Indian CopperLeaf_ Acalypha indica': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Indian Jujube_Ziziphus mauritiana': 'Leaves used in traditional medicine for their digestive properties.',
    'Indian Sarsaparilla_Hemidesmus indicus': 'Used in traditional medicine for its cooling and detoxifying properties.',
    'Indian Stinging Nettle_Urtica dioica subsp. gracilis': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Indian Thornapple_Datura metel': 'Used with caution in traditional medicine for its analgesic properties; toxic if ingested.',
    'Indian pennywort_Centella asiatica': 'Used in traditional medicine for its cognitive-enhancing properties.',
    'Indian wormwood_Artemisia indica': 'Used in traditional medicine for its digestive properties.',
    'Insulin': 'Likely referring to Costus igneus; leaves used in traditional medicine for their anti-diabetic properties.',
    'Ivy Gourd_Coccinia grandis': 'Consumed as a leafy vegetable and used in traditional medicine for its anti-diabetic properties.',
    'Jackfruit-Artocarpus heterophyllus': 'Leaves used in traditional medicine for their anti-diabetic properties.',
    'Jamaica Cherry-Gasagase_Muntingia calabura': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Jamun_Syzygium cumini': 'Leaves used in traditional medicine for their anti-diabetic properties.',
    'Jasmine-Jasmium': 'Leaves used in traditional medicine for their aromatic and anti-inflammatory properties.',
    'Kambajala': 'Likely a regional name; more information needed.',
    'Karanda_Carissa carandas': 'Leaves used in traditional medicine for their digestive properties.',
    'Kasambruga': 'Likely a regional name; more information needed.',
    'Kohlrabi-Brassica oleracea var. gongylodes': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Kokilaksha_Asteracantha longifolia': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Lagos Spinach_Celosia argentea': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Lambs Quarters_Chenopodium album': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Land Caltrops (Bindii)_Tribulus cistoides': 'Used in traditional medicine for its diuretic properties.',
    'Lantana- Lantana camara': 'Used with caution in traditional medicine; toxic if ingested.',
    'Lemon grass-Cymbopogon citratus': 'Leaves used in cooking and traditional medicine for their digestive and aromatic properties.',
    'Lemon-Citrus limon': 'Leaves used in traditional medicine for their aromatic and digestive properties.',
    'Lettuce Tree_Pisonia grandis': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Madagascar Periwinkle_Catharanthus roseus': 'Used in traditional medicine and for producing anticancer compounds.',
    'Madras Pea Pumpkin_Sesbania grandiflora': 'Leaves used in traditional medicine for their nutritional and anti-inflammatory properties.',
    'Malabar Catmint_Plectranthus amboinicus': 'Used in traditional medicine for its digestive and respiratory properties.',
    'Malabar_Nut-Justicia adhatoda': 'Used in traditional medicine for its respiratory benefits.',
    'Malabar_Spinach-Basella alba': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Mango_Mangifera indica': 'Leaves used in traditional medicine for their anti-diabetic properties.',
    'Marigold-Tagetes spp. (Genus)': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Mexican Mint_Plectranthus amboinicus (also known as Cuban Oregano)': 'Used in traditional medicine for its digestive and respiratory properties.',
    'Mexican Prickly Poppy_Argemone mexicana': 'Used with caution in traditional medicine; toxic if ingested.',
    'Mint-Mentha': 'Leaves used in cooking and traditional medicine for their digestive and aromatic properties.',
    'Mountain Knotgrass_Aerva lanata': 'Used in traditional medicine for its diuretic properties.',
    'Mustard_Brassica juncea': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Nagadali_Ruta graveolens': 'Used in traditional medicine for its anti-inflammatory and antispasmodic properties.',
    'Nalta Jute_Corchorus olitorius': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Neem_Azadirachta indica': 'Leaves used in traditional medicine for their antimicrobial and anti-inflammatory properties.',
    'Nelavembu-Andrographis paniculata': 'Used in traditional medicine for its immune-boosting and anti-inflammatory properties.',
    'Nerale': 'Likely a regional name; more information needed.',
    'Night blooming Cereus_Epiphyllum oxypetalum': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Nithyapushpa_Vinca rosea': 'Used in traditional medicine and for producing anticancer compounds.',
    'Nooni-Morinda citrifolia': 'Used in traditional medicine for its immune-boosting and anti-inflammatory properties.',
    'Oleander_Nerium oleander': 'Used with caution in traditional medicine; toxic if ingested.',
    'Onion-Allium cepa': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Padri': 'Likely a regional name; more information needed.',
    'Palak(Spinach)-Spinacia oleracea': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Panicled Foldwing_Dicliptera paniculata': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Pappaya-Carica papaya': 'Leaves used in traditional medicine for their digestive properties.',
    'Parijatha-Nyctanthes arbor-tristis': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Pea-Pisum sativum': 'Leaves used in cooking and traditional medicine for their nutritional properties.',
    'Peepal Tree_Ficus religiosa': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Pepper-Piper nigrum': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Pomegranate-Punica granatum': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Prickly Chaff Flower_Achyranthes aspera': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Pumpkin-Cucurbita pepo': 'Leaves used in cooking and traditional medicine for their nutritional properties.',
    'Punarnava_Boerhavia diffusa': 'Used in traditional medicine for its diuretic properties.',
    'Purple Fruited Pea Eggplant_Solanum trilobatum': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Purple Tephrosia_Tephrosia purpurea': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Raddish-Raphanus sativus': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Raktachandini_Pterocarpus santalinus': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Rasna_Alpinia galanga': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Rosary Pea_Abrus precatorius': 'Used with caution in traditional medicine; toxic if ingested.',
    'Rose Apple_Syzygium jambos': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Rose-Rosa': 'Leaves used in traditional medicine for their aromatic and anti-inflammatory properties.',
    'Roxburgh fig_Ficus auriculata': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Sampige': 'Likely a regional name; more information needed.',
    'Sandalwood_Santalum album': 'Leaves used in traditional medicine for their cooling and aromatic properties.',
    'Sapota-Manikara zapota': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Seethaashoka-Saraca asoca': 'Used in Ayurveda for treating gynecological disorders.',
    'Seethapala': 'Likely a regional name; more information needed.',
    'Shaggy button weed_Diodia teres': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Siru Keerai_Amaranthus tristis': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Small Water Clover_Marsilea minuta': 'Leaves used in traditional medicine for their cooling properties.',
    'Spiderwisp_Cleome viscosa': 'Used in traditional medicine for its digestive properties.',
    'Spinach1': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Square Stalked Vine_Sarcostemma acidum': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Stinking Passionflower_Passiflora foetida': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Sweet Basil_Ocimum basilicum': 'Leaves used in cooking and traditional medicine for their digestive and aromatic properties.',
    'Sweet flag_Acorus calamus': 'Leaves used in traditional medicine for their digestive properties.',
    'Tamarind_Tamarindus indica': 'Leaves used in cooking and traditional medicine for their digestive properties.',
    'Taro_Colocasia esculenta': 'Leaves consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Tecoma': 'Likely referring to Tecoma stans; used in traditional medicine for its anti-inflammatory properties.',
    'Thumbe': 'Likely a regional name; more information needed.',
    'Tinnevelly Senna_Cassia angustifolia (also known as Senna)': 'Leaves used in traditional medicine as a laxative.',
    'Tomato_Solanum lycopersicum': 'Leaves used in traditional medicine for their anti-inflammatory properties.',
    'Trellis Vine_Cissus sicyoides': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Trigonella Foenum-graecum (Fenugreek)': 'Used in cooking and traditional medicine for their digestive properties.',
    'Tulasi-Ocimum sanctum (also known as Holy Basil)': 'Used in traditional medicine for its immune-boosting and anti-inflammatory properties.',
    'Turmeric_ Curcuma longa': 'Leaves used in traditional medicine for their antimicrobial and anti-inflammatory properties.',
    'Velvet bean_Mucuna pruriens': 'Used in traditional medicine for its neurological benefits.',
    'Water Spinach_Ipomoea aquatica': 'Consumed as a leafy vegetable, rich in vitamins and minerals.',
    'Wood_sorel_ Oxalis spp': 'Leaves used in traditional medicine for their cooling properties.',
    'coatbuttons_Tridax procumbens': 'Used in traditional medicine for its wound healing and anti-inflammatory properties.',
    'other': 'Likely refers to unidentified or unspecified plants.',
    'Crape Jasmine-Tabernaemontana divaricata': 'Used in traditional medicine for its anti-inflammatory properties.',
    'Heart-leaved moonseed-Tinospora cordifolia': 'Used in traditional medicine for its immune-boosting properties.',
    'Indian Beech-Pongamia pinnata': 'Leaves used in traditional medicine for their antimicrobial properties.',
    'Kamakasturi': 'Likely a regional name; more information needed.',
    'Kepala': 'Likely a regional name; more information needed.'
}




@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/predict', methods=["POST"])
def Predict():
    imagefile = request.files['imagefile']
    image_path = "./images/" + imagefile.filename
    imagefile.save(image_path)


    try:
        # Load and preprocess the image
        img = image.load_img(image_path, target_size=(224, 224))
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array /= 255.0

        # Make predictions
        predictions = model.predict(img_array)
        predicted_class = np.argmax(predictions, axis=1)
        name = LeafName[predicted_class[0]]
        res = {
            "LeafName" : name,
            "Uses" : leaf_uses[name]
        }
    except Exception as e:
        print("Error:", e)
        res = {"error": str(e)}

    return jsonify(res)

if __name__ == '__main__':
    app.run(debug=True)
