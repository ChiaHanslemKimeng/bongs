import re

with open('templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Remove Journal from sidebar
content = re.sub(r'\s*<a href="{% url \'blog:post_list\' %}".*?>Journal</a>', '', content)

# Remove Best Sellers and New Arrivals from footer
content = re.sub(r'<li><a href="{% url \'shop:product_list\' %}" class="text-sm text-gray-400 hover:text-brand-accent">Best Sellers</a></li>\s*', '', content)
content = re.sub(r'<li><a href="{% url \'shop:product_list\' %}" class="text-sm text-gray-400 hover:text-brand-accent">New Arrivals</a></li>\s*', '', content)

# Replace the categories section in sidebar
sidebar_cats_pattern = r'{% for top_cat in shop_top_categories %}.*?{% endfor %}'
new_sidebar_cats = '''{% for top_cat in shop_top_categories %}
                    <div class="mb-2">
                        <a href="{% url 'shop:product_list_by_category' top_cat.slug %}" class="text-white hover:text-brand-accent block px-3 py-2 rounded-md font-semibold">{{ top_cat.name }}</a>
                        {% if top_cat.children.exists %}
                            <div class="pl-4 space-y-1 mt-1 border-l border-white/10 ml-4">
                                {% for child in top_cat.children.all %}
                                    <a href="{% url 'shop:product_list_by_category' child.slug %}" class="text-gray-300 hover:text-brand-accent block px-3 py-1 rounded-md text-sm">{{ child.name }}</a>
                                    {% if child.children.exists %}
                                        <div class="pl-4 space-y-1 mt-1">
                                            {% for subchild in child.children.all %}
                                                <a href="{% url 'shop:product_list_by_category' subchild.slug %}" class="text-gray-400 hover:text-brand-accent block px-3 py-1 rounded-md text-xs">- {{ subchild.name }}</a>
                                            {% endfor %}
                                        </div>
                                    {% endif %}
                                {% endfor %}
                            </div>
                        {% endif %}
                    </div>
                {% endfor %}'''

content = re.sub(sidebar_cats_pattern, new_sidebar_cats, content, flags=re.DOTALL)

with open('templates/base.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Done updating base.html')
