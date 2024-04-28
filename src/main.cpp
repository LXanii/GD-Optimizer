#include <Geode/Geode.hpp>
#include <Geode/modify/MenuLayer.hpp>
#include <Geode/modify/PlayLayer.hpp>

using namespace geode::prelude;
bool optimizerState;

std::array lowPriority = {"Discord.exe", "steamwebhelper.exe", "firefox.exe", "chrome.exe"};

class $modify(optimizerLayer, MenuLayer) {
	bool init() {
		if (!MenuLayer::init()) return false;
		optimizerState = Mod::get()->getSavedValue<bool>("state", true);

		auto optimizerButton = CCMenuItemSpriteExtra::create(CCSprite::createWithSpriteFrameName("GJ_reportBtn_001.png"), this, menu_selector(optimizerLayer::optimizerDisplay));
		auto menu = this->getChildByID("bottom-menu");

		menu->addChild(optimizerButton);
		menu->updateLayout();
		optimizerButton->setID("xanii.gd_optimizer/button");

		return true;
	}

	void optimizerDisplay(CCObject*) {
		if (optimizerState) createQuickPopup("GD Optimizer", "GD Optimizer is currently <cg>enabled</c>.\nWould you like to <cr>disable</c> GD Optimizer?", "Cancel", "Disable", [this](FLAlertLayer*, bool btn2) {
			if (btn2) optimizerState = false;
		});
		else createQuickPopup("GD Optimizer", "GD Optimizer is currently <cr>disabled</c>.\nWould you like to <cg>enable</c> GD Optimizer?", "Cancel", "Enable", [this](FLAlertLayer*, bool btn2) {
			if (btn2) optimizerState = true;
		});
		Mod::get()->setSavedValue<bool>("state", optimizerState);
	}
};

class $modify(PlayLayer) {
	bool init(GJGameLevel* level, bool useReplay, bool dontCreateObjects) {
		if (!PlayLayer::init(level, useReplay, dontCreateObjects)) return false;
		if (optimizerState) {
			for (int i = 0; i < sizeof(lowPriority)/sizeof(lowPriority[0]); i++) {
				std::string systemCommand = fmt::format("wmic process where name=\"{}\" CALL setpriority \"64\"", lowPriority[i]);
				system(systemCommand.c_str());
				log::info("{}", lowPriority[i]);
			}
		}
		return true;
	}
};