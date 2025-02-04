import logging as _logging
import json

from PyQt5.QtCore import pyqtSignal, QItemSelectionModel
from PyQt5.QtWidgets import (QHBoxLayout, QDialog, QPushButton, QPlainTextEdit, QFormLayout)

from sqlalchemy.sql import func

# from ..app.db import appdata_models as Am
from ..app.db import userdata_models as Um

logger = _logging.getLogger(__name__)


class MemoDialog(QDialog):

    accepted = pyqtSignal(dict)

    def __init__(self, text=''):
        super().__init__()
        self.setWindowTitle("Create Memo")

        self.front = QPlainTextEdit()
        self.front.setFixedSize(300, 50)
        self.front.textChanged.connect(self.unlock)

        self.back = QPlainTextEdit(text)
        self.back.setFixedSize(300, 50)
        self.back.textChanged.connect(self.unlock)

        self.add_btn = QPushButton('Add')
        self.add_btn.setDisabled(True)
        self.add_btn.clicked.connect(self.add_pressed)

        self.close_btn = QPushButton('Close')
        self.close_btn.clicked.connect(self.close_pressed)

        form = QFormLayout(self)

        form.addRow('Front', self.front)
        form.addRow('Back', self.back)

        self.buttons_layout = QHBoxLayout()
        self.buttons_layout.addWidget(self.add_btn)
        self.buttons_layout.addWidget(self.close_btn)

        form.addRow(self.buttons_layout)

    def not_blanks(self) -> bool:
        front = self.front.toPlainText()
        back = self.back.toPlainText()
        return front.strip() != '' and back.strip() != ''

    def unlock(self):
        if self.not_blanks():
            self.add_btn.setEnabled(True)
        else:
            self.add_btn.setDisabled(True)

    def add_pressed(self):
        values = {
            'Front': self.front.toPlainText(),
            'Back': self.back.toPlainText(),
        }
        self.accepted.emit(values)
        self.accept()

    def close_pressed(self):
        self.close()


class HasMemoDialog:
    def init_memo_dialog(self):
        self.memo_dialog_fields = {}

    def set_memo_dialog_fields(self, values):
        self.memo_dialog_fields = values

    def handle_create_memo_for_sutta(self):
        text = self.content_html.selectedText()

        deck = self._app_data.db_session.query(Um.Deck).first()

        self.memo_dialog_fields = {
            'Front': '',
            'Back': '',
        }

        d = MemoDialog(text)
        d.accepted.connect(self.set_memo_dialog_fields)
        d.exec_()

        if self.memo_dialog_fields['Front'] == '' or self.memo_dialog_fields['Back'] == '':
            return

        memo = Um.Memo(
            deck_id=deck.id,
            fields_json=json.dumps(self.memo_dialog_fields),
            created_at=func.now(),
        )

        try:
            self._app_data.db_session.add(memo)
            self._app_data.db_session.commit()

            schema = self._current_sutta.metadata.schema

            if self._current_sutta is not None:

                memo_assoc = Um.MemoAssociation(
                    memo_id=memo.id,
                    associated_table=f'{schema}.suttas',
                    associated_id=self._current_sutta.id,
                )

                self._app_data.db_session.add(memo_assoc)
                self._app_data.db_session.commit()

        except Exception as e:
            logger.error(e)

        if 'memos_sidebar' in self.features:
            # Add to model
            if self.model.memos:
                self.model.memos.append(memo)
            else:
                self.model.memos = [memo]

            index = self.model.index(len(self.model.memos) - 1)
            self.memos_list.selectionModel().select(index, QItemSelectionModel.Select)

            self.update_memos_list()

    def handle_create_memo_for_dict_word(self):
        text = self.content_html.selectedText()

        deck = self._app_data.db_session.query(Um.Deck).first()

        self.memo_dialog_fields = {
            'Front': '',
            'Back': '',
        }

        d = MemoDialog(text)
        d.accepted.connect(self.set_memo_dialog_fields)
        d.exec_()

        if self.memo_dialog_fields['Front'] == '' or self.memo_dialog_fields['Back'] == '':
            return

        memo = Um.Memo(
            deck_id=deck.id,
            fields_json=json.dumps(self.memo_dialog_fields),
            created_at=func.now(),
        )

        try:
            self._app_data.db_session.add(memo)
            self._app_data.db_session.commit()

            schema = self._current_word.metadata.schema

            if self._current_word is not None:

                memo_assoc = Um.MemoAssociation(
                    memo_id=memo.id,
                    associated_table=f'{schema}.dict_words',
                    associated_id=self._current_word.id,
                )

                self._app_data.db_session.add(memo_assoc)
                self._app_data.db_session.commit()

        except Exception as e:
            logger.error(e)

        if 'memos_sidebar' in self.features:
            # Add to model
            if self.model.memos:
                self.model.memos.append(memo)
            else:
                self.model.memos = [memo]

            index = self.model.index(len(self.model.memos) - 1)
            self.memos_list.selectionModel().select(index, QItemSelectionModel.Select)

            self.update_memos_list()
