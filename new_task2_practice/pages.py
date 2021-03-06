from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
from helpers import get_next_app


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class MyPage(Page):
    form_model = 'player'
    form_fields = ['newt2_weights']

    def vars_for_template(self):
        p = self.player
        p.for_template()
        return {'num_states': self.subsession.num_periods + 1}

    def before_next_page(self):
        self.player.newt2_get_outcome()




class Results(Page):
    def vars_for_template(self):
        return {'num_states': self.subsession.num_periods + 1}

    def app_after_this_page(player, upcoming_apps):
        player.participant.vars["step"] += 1
        return get_next_app(app_index=player.participant.vars["app_id"],
                            step=player.participant.vars["step"])

page_sequence = [Introduction, MyPage, Results]
