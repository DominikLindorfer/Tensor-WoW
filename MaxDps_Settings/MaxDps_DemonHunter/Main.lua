local addonName, addonTable = ...;
_G[addonName] = addonTable;

--- @type MaxDps
if not MaxDps then return end

local MaxDps = MaxDps;

local DemonHunter = MaxDps:NewModule('DemonHunter');
addonTable.DemonHunter = DemonHunter;

DemonHunter.spellMeta = {
	__index = function(t, k)
		print('Spell Key ' .. k .. ' not found!');
	end
}

function DemonHunter:Enable()
	if MaxDps.Spec == 1 then
		MaxDps.NextSpell = DemonHunter.Havoc;
		MaxDps:Print(MaxDps.Colors.Info .. 'DemonHunter - Havoc');
	elseif MaxDps.Spec == 2 then
		MaxDps.NextSpell = DemonHunter.Vengeance;
		MaxDps:Print(MaxDps.Colors.Info .. 'DemonHunter - Vengeance');
	end

	return true;
end