from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/api/blog-stats')
def get_blog_stats():
    stats = {
        "total_posts": 10,
        "top_performing_posts": [
            {
                "title": "Things to Do in a Small Town",
                "views": 1500,
                "category": "Road Trips"
            },
            {
                "title": "Road Trip Food Ideas - No Refrigeration Required",
                "views": 1200,
                "category": "Road Trips"
            },
            {
                "title": "Oklahoma Christmas Towns",
                "views": 1000,
                "category": "Small Town Travel Guides"
            }
        ],
        "monthly_visitors": 500,
        "trending_categories": ["Road Trips", "Small Town Travel Guides"],
        "top_states": ["Oklahoma", "Texas", "Kansas"]
    }
    return jsonify(stats)

@app.route('/api/va-tasks')
def get_va_tasks():
    tasks = {
        "pending_tasks": [
            {
                "id": 1,
                "title": "Research Small Towns in Texas Hill Country",
                "type": "research",
                "status": "pending",
                "due_date": "2024-01-15",
                "priority": "high"
            },
            {
                "id": 2,
                "title": "Optimize Images for Oklahoma Christmas Towns Post",
                "type": "image_optimization",
                "status": "pending",
                "due_date": "2024-01-20",
                "priority": "medium"
            },
            {
                "id": 3,
                "title": "Draft Road Trip Snacks for Summer Travel",
                "type": "content_writing",
                "status": "pending",
                "due_date": "2024-01-25",
                "priority": "medium"
            }
        ],
        "task_metrics": {
            "total_pending": 3,
            "by_type": {
                "research": 1,
                "image_optimization": 1,
                "content_writing": 1
            },
            "high_priority": 1
        }
    }
    return jsonify(tasks)

@app.route('/api/post-ideas', methods=["GET", "POST"]) # Test
def get_post_ideas():
    if request.method == "POST":
       new_idea = request.json
       print(new_idea)
    else:
        # Your existing GET logic should go here
    
    ideas = {
        "post_ideas": [
            {
                "title": "Best Oklahoma Towns to Visit in December",
                "keyword": "Best Places to Visit in December",
                "kd": 3,
                "volume": 1200
            },
            {
                "title": "Where to See Christmas Lights in Tulsa",
                "keyword": "Christmas Lights Near Me",
                "kd": 4,
                "volume": 34000
            },
            {
                "title": "Christmas Events in Missouri",
                "keyword": "Christmas Events Near Me",
                "kd": 1,
                "volume": 26000
            }


        ]
    }
    # Calculate total number of ideas
    
    total_ideas = len(ideas["post_ideas"])

    total_kd = 0
    total_volume = 0

    # Loop through ideas
    for idea in ideas["post_ideas"]:
        total_kd +=idea["kd"]
        total_volume += idea["volume"]

    # Calculate averages
    avg_kd = total_kd / total_ideas

    # Create metrics dictionary

    metrics = {
        "total_ideas": total_ideas,
        "average_kd": round(avg_kd, 1),
        "toatl_search_volumd": total_volume
    }

# Add metrics to response
    ideas["metrics"] = metrics

    return jsonify(ideas)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
