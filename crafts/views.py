from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import CraftPost, Comment
from .forms import CraftForm, CommentForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
def craft_list(request):
	craftposts = CraftPost.objects.filter(postcategory= "Craft").filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'crafts/craft_list.html', {'craftposts': craftposts})

def craft_detail(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			if comment.author:
				comment.name = comment.author
			else:
				comment.name = request.user
			comment.craftpost = craftpost
			comment.save()
			return redirect('crafts.views.craft_detail', pk=craftpost.pk)
	else:
		form = CommentForm()
	return render(request, 'crafts/craft_detail.html', {'form': form, 'craftpost':craftpost})


def food_list(request):
	foodposts = CraftPost.objects.filter(postcategory="Food").filter(published_date__lte=timezone.now()).order_by('-published_date')
	return render(request, 'crafts/food_list.html', {'foodposts': foodposts})

def food_detail(request, pk):
	foodpost = get_object_or_404(CraftPost, pk=pk)
	if request.method == "POST":
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = form.save(commit=False)
			if comment.author:
				comment.name = comment.author
			else:
				comment.name = request.user
			comment.craftpost = foodpost
			comment.save()
			return redirect('crafts.views.food_detail', pk=foodpost.pk)
	else:
		form = CommentForm()
	return render(request, 'crafts/food_detail.html', {'form': form, 'foodpost':foodpost})

@login_required
def craft_new(request):
	if request.method == "POST":
		form = CraftForm(request.POST, request.FILES)
		if form.is_valid():
			craftpost = form.save(commit=False)
			craftpost.author = request.user
			craftpost.save()
			if craftpost.postcategory == "Craft":
				return redirect('craft_detail', pk=craftpost.pk)
			elif craftpost.postcategory == "Food":
				return redirect('food_detail', pk=craftpost.pk)
	else:
		form = CraftForm()
	return render(request, 'crafts/craft_edit.html', {'form': form})

@login_required
def craft_edit(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	if request.method =="POST":
		form = CraftForm(request.POST, request.FILES, instance=craftpost, )
		if form.is_valid():
			craftpost = form.save(commit=False)
			craftpost.author = request.user
			craftpost.save()
			if craftpost.postcategory == "Craft":
				return redirect('craft_detail', pk=craftpost.pk)
			elif craftpost.postcategory == "Food":
				return redirect('food_detail', pk=craftpost.pk)
	else:
		form = CraftForm(instance=craftpost)
	return render(request, 'crafts/craft_edit.html', {'form': form})

@login_required
def craft_draft_list(request):
	draftposts = CraftPost.objects.filter(published_date__isnull=True).order_by('-created_date')
	return render(request, 'crafts/craft_draft_list.html', {'draftposts':draftposts})

@login_required
def craft_publish(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	craftpost.publish()
	if craftpost.postcategory == "Craft":
		return redirect('craft_detail', pk=pk)
	elif craftpost.postcategory == "Food":
		return redirect('food_detail', pk=pk)

	def publish(self):
		self.publish_date = timezone.now()
		self.save()

@login_required
def craft_remove(request, pk):
	craftpost = get_object_or_404(CraftPost, pk=pk)
	craftpost.delete()
	return redirect('crafts.views.craft_list')

# @login_required
# def add_comment_to_craft(request, pk):
# 	craftpost = get_object_or_404(CraftPost, pk=pk)
# 	if request.method == "POST":
# 		form = CommentForm(request.POST)
# 		if form.is_valid():
# 			comment = form.save(commit=False)
# 			comment.author = request.user
# 			comment.craftpost = craftpost
# 			comment.save()
# 			return redirect('crafts.views.craft_detail', pk=craftpost.pk)
# 	else:
# 		form = CommentForm()
# 	return render(request, 'crafts/add_comment_to_craft.html', {'form': form, 'craftpost':craftpost})

@login_required
def comment_approve(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	comment.approve()
	return redirect('crafts.views.craft_detail', pk=comment.craftpost.pk)

@login_required
def comment_remove(request, pk):
	comment = get_object_or_404(Comment, pk=pk)
	craft_pk = comment.craftpost.pk
	comment.delete()
	return redirect('crafts.views.craft_detail', pk=comment.craftpost.pk)

