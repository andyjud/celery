@login_required
def newsletter_subscribe(request):
    user = request.user
    user.profile.newsletter_subscribed = not user.profile.newsletter_subscribed
    user.profile.save()
    return redirect('profile-settings')
